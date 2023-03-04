migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("6g5odqch7ztl1nf")

  collection.type = "base"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("6g5odqch7ztl1nf")

  collection.type = ""

  return dao.saveCollection(collection)
})
