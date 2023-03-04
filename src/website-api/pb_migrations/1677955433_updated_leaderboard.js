migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("cwx1uj4x67ok8x7")

  collection.type = "base"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("cwx1uj4x67ok8x7")

  collection.type = ""

  return dao.saveCollection(collection)
})
