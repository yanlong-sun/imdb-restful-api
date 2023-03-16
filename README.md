# Movie/TV Show Information API

IMDb Datasets Description: https://www.imdb.com/interfaces/

## Endpoints

- [Retrieves a list of titles  
   `GET /api/name/`](#retrieves-a-list-of-titles)
- [Retrieves a list of names  
   `GET /api/name/`](#retrieves-a-list-of-names)
- [Retrieves a list of cast members for a specific title  
  `GET /api/title/<slug:tconst>/cast`](#retrieves-a-list-of-cast-members-for-a-specific-title)
- [Retrieves a list of alternate titles for a specific title  
  `GET /api/title/<slug:tconst>/akas`](#retrieves-a-list-of-alternate-titles-for-a-specific-title)
- [Retrieves a list of crew members for a specific title  
  `GET /api/title/<slug:tconst>/crew`](#retrieves-a-list-of-crew-members-for-a-specific-title)
- [Retrieves a list of episodes for a specific title  
   `GET /api/title/<slug:tconst>/episode`](#retrieves-a-list-of-episodes-for-a-specific-title)
- [Retrieves the ratings for a specific title  
  `GET /api/title/<slug:tconst>/ratings`](#retrieves-the-ratings-for-a-specific-title)

## Retrieves a list of titles.

##### `GET /api/title/`

Body:  
`tconst` (string) - alphanumeric unique identifier of the title  
`titleType` (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)  
`primaryTitle` (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release  
`originalTitle` (string) - original title, in the original language  
`isAdult` (boolean) - False: non-adult title; True: adult title  
`startYear` (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year  
`endYear` (YYYY) – TV Series end year. ‘’ for all other title types  
`runtimeMinutes` – primary runtime of the title, in minutes  
`genres` (string array) – includes up to three genres associated with the title

## Retrieves a list of names.

##### `GET /api/name/`

Body:  
`nconst` (string) - alphanumeric unique identifier of the name/person  
`primaryName` (string)– name by which the person is most often credited  
`birthYear` – in YYYY format  
`deathYear` – in YYYY format if applicable, else ''  
`primaryProfession` (array of strings)– the top-3 professions of the person  
`knownForTitles` (array of tconsts) – titles the person is known for

## Retrieves a list of cast members for a specific title.

##### `GET /api/title/<slug:tconst>/cast`

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:  
`tconst` (string) - alphanumeric unique identifier of the title  
`ordering` (integer) – a number to uniquely identify rows for a given titleId  
`nconst` (string) - alphanumeric unique identifier of the name/person  
`category` (string) - the category of job that person was in  
`job` (string) - the specific job title if applicable, else ''  
`characters` (string) - the name of the character played if applicable, else ''

## Retrieves a list of alternate titles for a specific title.

##### `GET /api/title/<slug:tconst>/akas`

Parameters:

- `tconst `(slug): Unique identifier for the title.

Body:  
`titleId` (string) - a tconst, an alphanumeric unique identifier of the title  
`ordering` (integer) – a number to uniquely identify rows for a given titleId  
`title` (string) – the localized title  
`region` (string) - the region for this version of the title  
`language` (string) - the language of the title  
`types` (array) - Enumerated set of attributes for this alternative title. One or more of the following: "alternative", "dvd", "festival", "tv", "video", "working", "original", "imdbDisplay"  
`attributes` (array) - Additional terms to describe this alternative title, not enumerated  
`isOriginalTitle` (boolean) – False: not original title; True: original title

## Retrieves a list of crew members for a specific title.

##### `GET /api/title/<slug:tconst>/crew`

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:  
`tconst` (string) - alphanumeric unique identifier of the title  
`directors` (array of nconsts) - director(s) of the given title  
`writers` (array of nconsts) – writer(s) of the given title

## Retrieves a list of episodes for a specific title.

##### `GET /api/title/<slug:tconst>/episode`

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:  
`tconst` (string) - alphanumeric identifier of episode  
`parentTconst` (string) - alphanumeric identifier of the parent TV Series  
`seasonNumber` (integer) – season number the episode belongs to  
`episodeNumber` (integer) – episode number of the tconst in the TV series

## Retrieves the ratings for a specific title.

##### `GET /api/title/<slug:tconst>/ratings`

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:  
`tconst` (string) - alphanumeric unique identifier of the title  
`averageRating` – weighted average of all the individual user ratings  
`numVotes` - number of votes the title has received
