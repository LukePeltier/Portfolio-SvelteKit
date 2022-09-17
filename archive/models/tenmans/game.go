package tenmans

import (
	"time"

	"gorm.io/gorm"
)

const (
	UndefinedWinner uint8 = iota
	BlueWins
	RedWins
)

type Game struct {
	gorm.Model
	Number           uint      `gorm:"unique" json:"number"`
	Nickname         string    `gorm:"unique" json:"nickname"`
	Winner           uint8     `json:"winner"`
	RandomTeams      bool      `json:"randomTeams"`
	MemeGame         bool      `json:"memeGame"`
	StartDate        time.Time `json:"startDate"`
	Duration         uint      `json:"duration"`
	RiotID           string    `json:"riotID"`
	SeasonID         uint
	Season           Season `json:"season"`
	EndedInSurrender bool   `json:"endedInSurrender"`
}

func (g Game) GetWinnerString() string {
	var returnString string
	switch g.Winner {
	case BlueWins:
		returnString = "Blue"
	case RedWins:
		returnString = "Red"
	default:
		returnString = "Undefined Winner"
	}
	return returnString
}
