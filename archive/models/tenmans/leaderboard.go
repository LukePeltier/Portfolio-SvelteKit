package tenmans

import (
	"fmt"
	"os"

	"github.com/hackebrot/turtle"
	"gorm.io/gorm"
)

type Leaderboard struct {
	gorm.Model
	Name 			string 	`gorm:"unique" json:"name"`
	ValueName 		string 	`gorm:"unique" json:"valueName"`
	Emoji			string 	`gorm:"unique" json:"emoji"`
	IsLifetime 		bool   	`json:"isLifetime"`
	ShortName		string	`gorm:"unique" json:"shortName"`
}

func GetEmojiCharFromName(name string) string {
	emoji, ok := turtle.Emojis[name]

	if !ok {
		fmt.Fprintf(os.Stderr, "no emoji found for name: %v\n", name)
		os.Exit(1)
	}

	return emoji.Char
}

func (l Leaderboard) GetEmojiChar() string {
	return GetEmojiCharFromName(l.Emoji)
}