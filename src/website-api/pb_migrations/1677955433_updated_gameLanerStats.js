migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("2ajjlshwdvhrp68")

  collection.type = "base"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("2ajjlshwdvhrp68")

  collection.type = ""

  return dao.saveCollection(collection)
})
