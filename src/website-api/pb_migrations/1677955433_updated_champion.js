migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("dzj727exya1jxhq")

  collection.type = "base"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("dzj727exya1jxhq")

  collection.type = ""

  return dao.saveCollection(collection)
})
