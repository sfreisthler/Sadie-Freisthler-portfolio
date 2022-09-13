import smartpy as sp


NAME = "GF_Ondemand_Collections"

class Error_message:
    def make(s): return (NAME + "_" + s)
    def not_admin():             return Error_message.make("NOT_ADMIN")
    def paused():                return Error_message.make("PAUSED")

class Collection:
    def get_type():
        return sp.TRecord(
            active = sp.TNat,
            title = sp.TString,
            description = sp.TString,
            max_generated = sp.TNat,
            price = sp.TMutez,
            creator_address = sp.TAddress,
            num_minted = sp.TNat,
            deleted = sp.TNat,
        ).layout(("active", ("title", ("description", ("max_generated", ("price", ("creator_address", ("num_minted", "deleted"))))))))
    def make(active, title, description, max_generated, price, creator_address, num_minted, deleted):
        return sp.record(
            active = active,
            title = title,
            description = description,
            max_generated = max_generated,
            price = price,
            creator_address = creator_address,
            num_minted = num_minted,
            deleted = deleted,
        )

class FA2_core(sp.Contract):
    def __init__(self, metadata, **extra_storage):
        self.add_flag("lazy-entry-points")
        self.add_flag("initial-cast")
        self.exception_optimization_level = "default-line"

        self.init(
            collections = sp.map(tvalue = Collection.get_type()), # list of each minted collection
            collection_tokens = sp.big_map(tkey = sp.TNat, tvalue = sp.TSet(t = sp.TNat)), # collection_id => set(token_ids)
            num_collections = 0,
            metadata = metadata,
            **extra_storage
        )

    @sp.entry_point
    def mutez_transfer(contract, params):
        sp.verify(sp.sender == contract.data.administrator, message = Error_message.not_admin())
        sp.set_type(params.destination, sp.TAddress)
        sp.set_type(params.amount, sp.TMutez)
        sp.send(params.destination, params.amount)

    def is_paused(self):
        return self.data.paused

    @sp.entry_point
    def set_pause(self, params):
        sp.verify(self.is_administrator(sp.sender), message = Error_message.not_admin())
        self.data.paused = params

    def is_administrator(self, sender):
        return sender == self.data.administrator

    @sp.entry_point
    def set_administrator(self, params):
        sp.verify(self.is_administrator(sp.sender), message = Error_message.not_admin())
        self.data.administrator = params

    @sp.entry_point
    def set_metadata(self, k, v):
        sp.verify(self.is_administrator(sp.sender), message = Error_message.not_admin())
        self.data.metadata[k] = v

    @sp.entry_point
    def create_collection(self, req):
        sp.set_type(req, Collection.get_type())
        sp.verify(self.is_administrator(sp.sender), message = Error_message.not_admin())

        collection_id = self.data.num_collections
        self.data.collections[collection_id] = Collection.make(
            active = req.active,
            title = req.title,
            description = req.description,
            max_generated = req.max_generated,
            price = req.price,
            creator_address = req.creator_address,
            num_minted = req.num_minted,
            deleted = req.deleted,
        )
        self.data.collection_tokens[collection_id] = sp.set(t = sp.TNat)
        self.data.num_collections = self.data.num_collections + 1

    @sp.entry_point
    def update_collection(self, req):
        sp.set_type(req, sp.TRecord(
            collection_id = sp.TNat,
            collection = Collection.get_type(),
        )).layout(("collection_id", "collection"))

        sp.verify(self.is_administrator(sp.sender), message = Error_message.not_admin())
        sp.verify(self.data.collections.contains(req.collection_id), message = Error_message.make('Unknown collection'))

        self.data.collections[req.collection_id] = Collection.make(
            active = req.collection.active,
            title = req.collection.title,
            description = req.collection.description,
            max_generated = req.collection.max_generated,
            price = req.collection.price,
            creator_address = req.collection.creator_address,
            num_minted = req.collection.num_minted,
            deleted = req.collection.deleted,
        )

    @sp.entry_point
    def delete_collection(self, collection_id):
        sp.verify(self.is_administrator(sp.sender), message = Error_message.not_admin())
        sp.verify(self.data.collections.contains(collection_id), message = Error_message.make('Unknown collection'))
        self.data.collections[collection_id].deleted = 1
        self.data.collections[collection_id].active = 0

    @sp.entry_point
    def purchase(self, collection_id):
        sp.verify( ~self.is_paused(), message = Error_message.paused() )
        sp.verify(collection_id >= 0, message = "negative collection_id")
        sp.verify(collection_id < self.data.num_collections, message = "invalid collection_id")
        sp.verify(self.data.collections[collection_id].deleted == 0, message = "collection is deleted")
        sp.verify(self.data.collections[collection_id].num_minted < self.data.collections[collection_id].max_generated, message = "cannot mint more tokens in that collection")
        sp.verify(sp.amount == self.data.collections[collection_id].price, message = "must pay full price")

        token_id = self.data.num_tokens
        self.data.collections[collection_id].num_minted = self.data.collections[collection_id].num_minted + 1



class FA2(FA2_core):


    def __init__(self, metadata, admin):
        list_of_views = [
        ]

        metadata_base = {
            "name": "Glitch Forge Collections",
            "version": "1.0.0",
            "description": "Glitch Forge's NFT Collections",
            "authors": [ "Glitch Forge <https://glitchforge.xyz>" ],
            "homepage": "https://glitchforge.xyz",
            "interfaces": [
                "TZIP-012",
                "TZIP-016",
                "TZIP-021",
            ],
            "views": list_of_views
        }

        FA2_core.__init__(self, metadata, paused = False, administrator = admin)
        self.init_metadata("metadata", metadata_base)





## ## Tests
##
## ### Auxiliary Consumer Contract
##
## This contract is used by the tests to be on the receiver side of
## callback-based entry-points.
## It stores facts about the results in order to use `scenario.verify(...)`
## (cf.
##  [documentation](https://smartpy.io/docs/scenarios/testing)).
class View_consumer(sp.Contract):
    def __init__(self, contract):
        self.contract = contract
        self.init(last_sum = 0, operator_support = False);

    @sp.entry_point
    def reinit(self):
        self.data.last_sum = 0
        # It's also nice to make this contract have more than one entry point.

    @sp.entry_point
    def receive_balances(self, params):
        sp.set_type(params, Balance_of.response_type())
        self.data.last_sum = 0
        sp.for resp in params:
            self.data.last_sum += resp.balance

# ### Generation of Test Scenarios
#
# Tests are also parametrized by the `FA2_config` object.
# The best way to visualize them is to use the online IDE
# (<https://www.smartpy.io/ide/>).
def add_test(is_default = True):
    @sp.add_test(name = "TESTS_"+NAME, is_default = is_default)
    def test():
        scenario = sp.test_scenario()
        scenario.h1("Glitch Forge Tests")
        scenario.table_of_contents()
        # sp.test_account generates ED25519 key-pairs deterministically:
        admin = sp.test_account("Administrator")
        alice = sp.test_account("Alice")
        bob   = sp.test_account("Robert")

        # Let's display the accounts:
        scenario.h2("Accounts")
        scenario.show([admin, alice, bob])
        c1 = FA2(metadata = sp.utils.metadata_of_url("https://example.com"),
                 admin = admin.address)
        scenario += c1

        tok0_md = sp.map(l = {
            "" : sp.utils.bytes_of_string("ipfs://some_hash_here")
        })


        scenario.h2("Cant update non-existing collection...")
        c1.update_collection(collection_id = 5, collection = Collection.make(
            active = 1,
            title = 'Testy',
            description = 'testersons',
            max_generated = 100,
            price = sp.tez(100),
            creator_address = admin.address,
            num_minted = 0,
            deleted = 0,
        )).run(sender = admin, valid=False)


        scenario.h2("Non-admin can't create collections...");
        c1.create_collection(Collection.make(
            active = 1,
            title = 'Testy',
            description = 'testersons',
            max_generated = 100,
            price = sp.tez(100),
            creator_address = admin.address,
            num_minted = 0,
            deleted = 0,
        )).run(sender = alice, valid=False)

        scenario.h2("Admin Can Create Collections...");
        c1.create_collection(Collection.make(
            active = 0,
            title = 'Testy',
            description = 'testersons',
            max_generated = 100,
            price = sp.tez(100),
            creator_address = admin.address,
            num_minted = 0,
            deleted = 0,
        )).run(sender = admin, valid=True)

        c1.create_collection(Collection.make(
            active = 0,
            title = 'Testy2',
            description = 'testersons2',
            max_generated = 100,
            price = sp.tez(100),
            creator_address = admin.address,
            num_minted = 0,
            deleted = 0,
        )).run(sender = admin, valid=True)


        scenario.h2("non-admin can't update...")
        c1.update_collection(collection_id = 0, collection = Collection.make(
            active = 1,
            title = 'TestyUpdated',
            description = 'testersons update!',
            max_generated = 2,
            price = sp.tez(5),
            creator_address = admin.address,
            num_minted = 0,
            deleted = 0,
        )).run(sender = alice, valid=False)

        scenario.h2("admin can update...")
        c1.update_collection(collection_id = 0, collection = Collection.make(
            active = 1,
            title = 'TestyUpdated',
            description = 'testersons update!',
            max_generated = 2,
            price = sp.tez(5),
            creator_address = admin.address,
            num_minted = 0,
            deleted = 0,
        )).run(sender = admin, valid=True)

        scenario.verify(c1.data.collections[0].active == 1)
        scenario.verify(c1.data.collections[0].title == 'TestyUpdated')
        scenario.verify(c1.data.collections[0].max_generated == 2)
        scenario.verify(c1.data.collections[0].price == sp.tez(5))


        scenario.h2("Invalid Minting (incorrect price)...");
        c1.purchase(0).run(sender = alice, amount = sp.tez(1), valid=False)
        c1.purchase(0).run(sender = alice, amount = sp.tez(100), valid=False)

        scenario.h2("Invalid Minting (incorrect collection)...");
        c1.purchase(999).run(sender = alice, amount = sp.tez(5), valid=False)

        scenario.h2("Minting tokens...");
        c1.purchase(0).run(sender = alice, amount = sp.tez(5), valid=True)
        c1.purchase(0).run(sender = bob, amount = sp.tez(5), valid=True)

        scenario.h2("Cant mint more...");
        c1.purchase(0).run(sender = alice, amount = sp.tez(5), valid=False)


        scenario.table_of_contents()

        # delete_collection tests
        scenario.h2("non-admin can't delete...");
        c1.delete_collection(0).run(sender= alice, amount = sp.tez(5), valid=False)

        scenario.h2("admin can delete...");
        c1.delete_collection(0).run(sender= admin, amount = sp.tez(5), valid=True)

        scenario.h2("Cant purchase deleted collections...");
        c1.purchase(0).run(sender= alice, amount = sp.tez(5), valid=False)

##
## ## Global Environment Parameters
##
## The build system communicates with the python script through
## environment variables.
## The function `environment_config` creates an `FA2_config` given the
## presence and values of a few environment variables.
def global_parameter(env_var, default):
    try:
        if os.environ[env_var] == "true" :
            return True
        if os.environ[env_var] == "false" :
            return False
        return default
    except:
        return default

## ## Standard “main”
##
## This specific main uses the relative new feature of non-default tests
## for the browser version.
if "templates" not in __name__:
    add_test()

    sp.add_compilation_target(NAME+"_comp", FA2(
                              metadata = sp.utils.metadata_of_url("ipfs://REPLACE_ME_IPFS"), # generated from "ipfs add contract_metadata.json"
                              admin = sp.address("REPLACE_ME_ADMIN"))) # server wallet
