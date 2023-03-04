migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("7ee39s42vtaiwjx")

  collection.type = "base"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("7ee39s42vtaiwjx")

  collection.type = ""

  return dao.saveCollection(collection)
})
