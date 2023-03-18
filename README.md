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

<ul>
<li>`count` (integer) - total number of titles returned  </li>
<li>`next` (url) - the link of the next page of the result  </li>
<li>`previous` (url) - the link of the previous page of the result  </li>
<li>`result` (list) - [</li>
  <ul>
<li>`tconst` (string) - alphanumeric unique identifier of the title</li>
<li>`titleType` (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)</li>
<li>`primaryTitle` (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release</li>
<li>`originalTitle` (string) - original title, in the original language</li>
<li>`isAdult` (boolean) - False: non-adult title; True: adult title</li>
<li>`startYear` (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year</li>
<li>`endYear` (YYYY) – TV Series end year. ‘’ for all other title types</li>
<li>`runtimeMinutes` – primary runtime of the title, in minutes</li>
<li>`genres` (string array) – includes up to three genres associated with the title</li>
 </ul>
]</ul>

## Retrieves a list of names.

##### `GET /api/name/`

Body:

<ul>
<li>`count` (integer) - total number of titles returned  </li>
<li>`next` (url) - the link of the next page of the result  </li>
<li>`previous` (url) - the link of the previous page of the result  </li>
<li>`result` (list) - [</li>
  <ul>
<li>`nconst` (string) - alphanumeric unique identifier of the name/person  </li>
<li>`primaryName` (string)– name by which the person is most often credited  </li>
<li>`birthYear` – in YYYY format  </li>
<li>`deathYear` – in YYYY format if applicable, else ''  </li>
<li>`primaryProfession` (array of strings)– the top-3 professions of the person  </li>
`knownForTitles` (array of tconsts) – titles the person is known for</li>
</ul>
]</ul>
## Retrieves a list of cast members for a specific title.

##### `GET /api/title/<slug:tconst>/cast`

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:

<ul>
<li>`count` (integer) - total number of titles returned  </li>
<li>`next` (url) - the link of the next page of the result  </li>
<li>`previous` (url) - the link of the previous page of the result  </li>
<li>`result` (list) - [</li>
  <ul>
<li>`tconst` (string) - alphanumeric unique identifier of the title  </li>
<li>`ordering` (integer) – a number to uniquely identify rows for a given titleId  </li>
<li>`nconst` (string) - alphanumeric unique identifier of the name/person  </li>
<li>`category` (string) - the category of job that person was in  </li>
<li>`job` (string) - the specific job title if applicable, else ''  </li>
<li>`characters` (string) - the name of the character played if applicable, else ''</li>
</ul>
]</ul>

## Retrieves a list of alternate titles for a specific title.

##### `GET /api/title/<slug:tconst>/akas`

Parameters:

- `tconst `(string): Unique identifier for the title.

Body:

<ul>
<li>`count` (integer) - total number of titles returned  </li>
<li>`next` (url) - the link of the next page of the result  </li>
<li>`previous` (url) - the link of the previous page of the result  </li>
<li>`result` (list) - [</li>
  <ul>
<li>`titleId` (string) - a tconst, an alphanumeric unique identifier of the title </li> 
<li>`ordering` (integer) – a number to uniquely identify rows for a given titleId </li> 
<li>`title` (string) – the localized title  </li>
<li>`region` (string) - the region for this version of the title  </li>
<li>`language` (string) - the language of the title  </li>
<li>`types` (array) - Enumerated set of attributes for this alternative title. One or more of the following: "alternative", "dvd", "festival", "tv", "video", "working", "original", "imdbDisplay"  </li>
<li>`attributes` (array) - Additional terms to describe this alternative title, not enumerated  </li>
<li>`isOriginalTitle` (boolean) – False: not original title; True: original title</li>
</ul>
]</ul>

## Retrieves a list of crew members for a specific title.

##### `GET /api/title/<slug:tconst>/crew`

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:

<ul>
<li>`count` (integer) - total number of titles returned  </li>
<li>`next` (url) - the link of the next page of the result  </li>
<li>`previous` (url) - the link of the previous page of the result  </li>
<li>`result` (list) - [</li>
  <ul>
<li>`tconst` (string) - alphanumeric unique identifier of the title  </li>
<li>`directors` (array of nconsts) - director(s) of the given title  </li>
<li>`writers` (array of nconsts) – writer(s) of the given title</li>
</ul>
]</ul>

## Retrieves a list of episodes for a specific title.

##### `GET /api/title/<slug:tconst>/episode`

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:

<ul>
<li>`count` (integer) - total number of titles returned  </li>
<li>`next` (url) - the link of the next page of the result  </li>
<li>`previous` (url) - the link of the previous page of the result  </li>
<li>`result` (list) - [</li>
  <ul>
<li>`tconst` (string) - alphanumeric identifier of episode  </li>
<li>`parentTconst` (string) - alphanumeric identifier of the parent TV Series  </li>
<li>`seasonNumber` (integer) – season number the episode belongs to  </li>
<li>`episodeNumber` (integer) – episode number of the tconst in the TV series</li>
</ul>
]</ul>

## Retrieves the ratings for a specific title.

##### `GET /api/title/<slug:tconst>/ratings`

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:

<ul>
<li>`count` (integer) - total number of titles returned  </li>
<li>`next` (url) - the link of the next page of the result  </li>
<li>`previous` (url) - the link of the previous page of the result  </li>
<li>`result` (list) - [</li>
  <ul>
<li>`tconst` (string) - alphanumeric unique identifier of the title  </li>
<li>`averageRating` – weighted average of all the individual user ratings  </li>
<li>`numVotes` - number of votes the title has received</li>
</ul>
]</ul>
