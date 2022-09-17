package tenmans

import (
	"gorm.io/gorm"
)

func SetupTenMansDB(db *gorm.DB) {
	db.AutoMigrate(&Season{}, &Game{}, &Leaderboard{})
}
