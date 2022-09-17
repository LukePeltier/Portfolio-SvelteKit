package models

import (
	tenmans "lukepeltier/website-api/models/tenmans"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var DB *gorm.DB

func SetupWebsiteDB() {
	DB, err := gorm.Open(sqlite.Open("website.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	// Setup ten mans db
	tenmans.SetupTenMansDB(DB)
}
