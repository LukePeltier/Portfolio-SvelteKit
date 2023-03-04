migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("rhq6acuxsmqi5k7")

  collection.type = "base"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("rhq6acuxsmqi5k7")

  collection.type = ""

  return dao.saveCollection(collection)
})
