migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("systemprofiles0")

  collection.name = "users"
  collection.type = "auth"
  collection.system = false
  collection.listRule = "id = @request.auth.id"
  collection.viewRule = "id = @request.auth.id"
  collection.createRule = ""
  collection.updateRule = "id = @request.auth.id"
  collection.options = {
    "allowEmailAuth": true,
    "allowOAuth2Auth": true,
    "allowUsernameAuth": false,
    "exceptEmailDomains": null,
    "manageRule": null,
    "minPasswordLength": 8,
    "onlyEmailDomains": null,
    "requireEmail": true
  }

  // remove
  collection.schema.removeField("pbfielduser")

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("systemprofiles0")

  collection.name = "profiles"
  collection.type = ""
  collection.system = true
  collection.listRule = null
  collection.viewRule = null
  collection.createRule = null
  collection.updateRule = null
  collection.options = {}

  // add
  collection.schema.addField(new SchemaField({
    "system": true,
    "id": "pbfielduser",
    "name": "userId",
    "type": "user",
    "required": true,
    "unique": true,
    "options": {
      "maxSelect": 1,
      "cascadeDelete": true
    }
  }))

  return dao.saveCollection(collection)
})
