### Movie/TV Show Information API

#### Endpoints

##### `GET /api/title/`

##### Retrieves a list of titles.

Parameters:  
 None

Body:
`titleId` (string) - a tconst, an alphanumeric unique identifier of the title
`ordering` (integer) – a number to uniquely identify rows for a given titleId
`title` (string) – the localized title
`region` (string) - the region for this version of the title
`language` (string) - the language of the title
`types` (array) - Enumerated set of attributes for this alternative title. One or more of the following: "alternative", "dvd", "festival", "tv", "video", "working", "original", "imdbDisplay". New values may be added in the future without warning
`attributes` (array) - Additional terms to describe this alternative title, not enumerated
`isOriginalTitle` (boolean) – False: not original title; True: original title

##### `GET /api/name/`

##### Retrieves a list of names.

Parameters:

- None  
  Body:

`nconst` (string) - alphanumeric unique identifier of the name/person
`primaryName` (string)– name by which the person is most often credited
`birthYear` – in YYYY format
`deathYear` – in YYYY format if applicable, else ''
`primaryProfession` (array of strings)– the top-3 professions of the person
`knownForTitles` (array of tconsts) – titles the person is known for

##### `GET /api/title/<slug:tconst>/cast`

##### Retrieves a list of cast members for a specific title.

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:

`name` (string): Name of the cast member.
`character` (string): Name of the character played by the cast member.

##### `GET /api/title/<slug:tconst>/cast`

##### Retrieves a list of cast members for a specific title.

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:

`name` (string): Name of the cast member.
`character` (string): Name of the character played by the cast member.

##### `GET /api/title/<slug:tconst>/akas`

##### Retrieves a list of alternate titles for a specific title.

Parameters:

- `tconst `(slug): Unique identifier for the title.

Body:

`title `(string): Name of the alternate title.

##### `GET /api/title/<slug:tconst>/crew`

##### Retrieves a list of crew members for a specific title.

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:

name (string): Name of the crew member.
job (string): Job position of the crew member.

##### `GET /api/title/<slug:tconst>/episode`

##### Retrieves a list of episodes for a specific title.

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:

season_number (integer): Number of the season the episode belongs to.
episode_number (integer): Number of the episode within the season.
title (string): Name of the episode.

##### `GET /api/title/<slug:tconst>/ratings`

##### Retrieves the ratings for a specific title.

Parameters:

- `tconst` (string): Unique identifier for the title.

Body:

rating (float): The rating given to the title (out of 10).
