from django.db import models
from django.db.models import Sum
from random import shuffle


# Create your models here.
class Player(models.Model):
    playerName = models.TextField(unique=True)

    def getMostPlayedCharacterString(self):
        charCounts = self.getCharactersPlayed()
        charNames = []
        currentMax = 0
        for char, count in charCounts.items():
            if(count < currentMax):
                continue
            elif(count == currentMax):
                charNames.append(char)
            elif(count > currentMax):
                currentMax = count
                charNames.clear()
                charNames.append(char)
        return "/".join(sorted(charNames)) + " ({} tournaments)".format(currentMax)

    def getCharactersPlayed(self):
        gamesPlayed = TournamentEntry.objects.filter(
            player__exact=self.id)
        charCounts = {}
        for entry in gamesPlayed:
            characterName = entry.character.characterName
            if(characterName in charCounts):
                charCounts[characterName] += 1
            else:
                charCounts[characterName] = 1
        return charCounts

    def getBestPerformingCharacterString(self):
        tournamentsPlayed = TournamentEntry.objects.filter(player__exact=self.id)
        charsPlayed = []
        for entry in tournamentsPlayed:
            character = entry.character
            if(character not in charsPlayed):
                charsPlayed.append(character)
        currentMin = float('inf')
        charString = []
        for char in charsPlayed:
            powerRank = self.getPowerRankingPercentage(char)
            if(powerRank > currentMin):
                continue
            elif(powerRank == currentMin):
                charString.append(char.characterName)
            elif(powerRank < currentMin):
                currentMin = powerRank
                charString.clear()
                charString.append(char.characterName)
        return "/".join(sorted(charString)) + \
            " (Filtered Power Ranking: Top {}%)".format(currentMin * 100)

    def getPowerRankingPercentage(self, character=None):
        if character is not None:
            tournamentsPlayed = TournamentEntry.objects.filter(player__exact=self.id, character__exact=character.id)
        else:
            tournamentsPlayed = TournamentEntry.objects.filter(player__exact=self.id)

        totalTournamentCount = tournamentsPlayed.count()
        if totalTournamentCount == 0:
            return None
        totalRankPercent = 0
        for entry in tournamentsPlayed.iterator():
            entry: TournamentEntry
            numOfPlayersInTournament = TournamentEntry.objects.filter(tournament__exact=entry.tournament.id).count()
            entryRankWeighted = (entry.getPlacement()[0]) / (numOfPlayersInTournament)
            totalRankPercent += entryRankWeighted

        return round(totalRankPercent / totalTournamentCount, 5)

    def getTotalTournamentsPlayed(self):
        return TournamentEntry.objects.filter(player__exact=self.id).count()

    def getTotalHolesPlayed(self):
        return TournamentEntryHole.objects.filter(tournamentEntry__player__exact=self.id).count()

    def getUniqueCharacterCount(self):
        charCounts = self.getCharactersPlayed()
        return len(charCounts)

    def getPlacementInTournament(self, tournament):
        entry = TournamentEntry.objects.filter(tournament__exact=tournament.id, player__exact=self.id).first()
        if entry is None:
            return None
        entry: TournamentEntry
        return entry.getPlacement()

    def getTournamentRate(self):
        players = Player.objects.all()
        topNumber = 0
        for player in players:
            count = player.getTotalTournamentsPlayed()
            if(count > topNumber):
                topNumber = count
        playerNumber = self.getTotalTournamentsPlayed()
        return round(playerNumber / topNumber, 3)

    def getPowerRankings():
        players = list(Player.objects.all())
        shuffle(players)
        Player.quickSort(players, 0, len(players) - 1)
        return players

    def partition(arr, low, high):
        i = (low - 1)         # index of smaller element
        pivot = arr[high]     # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if Player.comparePlayers(arr[j], pivot) <= 0:

                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    # The main function that implements QuickSort
    # arr[] --> Array to be sorted,
    # low  --> Starting index,
    # high  --> Ending index

    # Function to do Quick sort
    def quickSort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:

            # pi is partitioning index, arr[p] is now
            # at right place
            pi = Player.partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            Player.quickSort(arr, low, pi - 1)
            Player.quickSort(arr, pi + 1, high)

    def comparePlayers(playerOne: 'Player', playerTwo: 'Player'):
        tournaments = Tournament.objects.all()

        totalScore = 0

        for tournament in tournaments:
            playerOnePlacement = playerOne.getPlacementInTournament(tournament)
            playerTwoPlacement = playerTwo.getPlacementInTournament(tournament)
            numOfHoles = tournament.numOfHoles
            lastPlaceScore = tournament.getLastPlaceDict()[2] + (1 * (numOfHoles / 18))

            if playerOnePlacement is None and playerTwoPlacement is None:
                continue

            elif playerOnePlacement is None and playerTwoPlacement is not None:
                totalScore += (lastPlaceScore - playerTwoPlacement[2]) / (numOfHoles / 18)

            elif playerOnePlacement is not None and playerTwoPlacement is None:
                totalScore += (playerOnePlacement[2] - lastPlaceScore) / (numOfHoles / 18)

            else:
                totalScore += (playerOnePlacement[2] - playerTwoPlacement[2]) / (numOfHoles / 18)

        if totalScore == 0:
            return playerTwo.getTotalHolesPlayed() - playerOne.getTotalHolesPlayed()

        return totalScore


class Character(models.Model):
    characterName = models.TextField(unique=True)
    fullImageName = models.TextField(null=True)
    characterPrimaryColor = models.TextField(default="#ff0001")


class CharacterStats(models.Model):
    TYPE_CHOICES = (
        ('SPEED', "Speed"),
        ('POWER', "Power"),
        ('CONTROL', "Control"),
        ('SPIN', "Spin"),
        ('ALL-ROUND', "All-Round")
    )
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    characterType = models.TextField(choices=TYPE_CHOICES)
    characterPower = models.PositiveIntegerField()
    character2StarPower = models.PositiveIntegerField(null=True)


class Course(models.Model):
    courseName = models.TextField(unique=True)
    courseDescription = models.TextField(null=True)
    courseGlyph = models.TextField(null=True)


class Hole(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    holeNumber = models.PositiveSmallIntegerField()
    par = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (('course', 'holeNumber'))


class TournamentType(models.Model):
    typeName = models.TextField(unique=True)


class Tournament(models.Model):
    name = models.TextField(unique=True)
    startDate = models.DateTimeField(default='current_timestamp()')
    endDate = models.DateTimeField(null=True)
    tournamentType = models.ForeignKey(TournamentType, on_delete=models.CASCADE)
    numOfHoles = models.PositiveSmallIntegerField()

    def getPlacementDict(self):
        allEntries = TournamentEntry.objects.filter(tournament__exact=self.id)

        scores = {}

        for entry in allEntries:
            scores[entry.player.playerName] = (entry.getShotsTotal(), entry.getScore(), entry.character.characterName)

        sortedScores = {k: (v, w, z) for k, (v, w, z) in sorted(scores.items(), key=lambda item: item[1])}

        result = {}
        prev = None
        i = 0
        j = 0
        for name, (shots, score, characterName) in sortedScores.items():
            i += 1
            if shots != prev:
                j = i
                place, prev = i, shots
            else:
                place, prev = j, shots

            result[name] = (place, shots, score, characterName)
        return result

    def getLastPlaceDict(self):
        placementDict = self.getPlacementDict()

        lastPlace = 0
        lastPlaceDict = None
        for name, (ranking, shotsTaken, score, characterName) in placementDict.items():
            if ranking > lastPlace:
                lastPlace = ranking
                lastPlaceDict = (ranking, shotsTaken, score, characterName)
        return lastPlaceDict


class TournamentHole(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()


class TournamentEntry(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def getPlacement(self):
        return self.tournament.getPlacementDict()[self.player.playerName]

    def getShotsTotal(self):
        return TournamentEntryHole.objects.filter(tournamentEntry__exact=self.id).aggregate(Sum('shotsTaken'))['shotsTaken__sum']

    def getScore(self):
        holesInTourney = TournamentHole.objects.filter(tournament__exact=self.tournament.id)
        sumPar = 0
        for hole in holesInTourney:
            hole: TournamentHole
            sumPar += hole.hole.par

        return self.getShotsTotal() - sumPar

    class Meta:
        unique_together = (('tournament', 'player'))


class TournamentEntryHole(models.Model):
    tournamentEntry = models.ForeignKey(TournamentEntry, on_delete=models.CASCADE)
    tournamentHole = models.ForeignKey(TournamentHole, on_delete=models.CASCADE)
    shotsTaken = models.PositiveSmallIntegerField()
    approved = models.BooleanField(default=False)

    class Meta:
        unique_together = (('tournamentHole', 'tournamentEntry'))
