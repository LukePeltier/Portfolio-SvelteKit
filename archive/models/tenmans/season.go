package tenmans

import "gorm.io/gorm"

type Season struct {
	gorm.Model
	Number 		uint8 	`gorm:"unique" json:"number"`
	Nickname	string 	`gorm:"unique" json:"nickname"`
}