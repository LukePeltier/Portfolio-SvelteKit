migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("3dqyslyagpuw144")

  collection.type = "base"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("3dqyslyagpuw144")

  collection.type = ""

  return dao.saveCollection(collection)
})
