migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("i49u5vfey7ohdgh")

  collection.type = "base"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("i49u5vfey7ohdgh")

  collection.type = ""

  return dao.saveCollection(collection)
})
