migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ku4usj8dtshvvcl")

  collection.type = "base"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ku4usj8dtshvvcl")

  collection.type = ""

  return dao.saveCollection(collection)
})
