import fresh_tomatoes
import media

# Movie Class Constructor for The Dark Knight Movie
the_dark_knight = media.Movie("The Dark Knight",
                              "With the help of allies Lt. Jim Gordon"
                              "(Gary Oldman)and DA Harvey Dent"
                              " (Aaron Eckhart),Batman (Christian"
                              " Bale) has been able to keep a tight"
                              " lid on crime in Gotham City. But when"
                              " a vile young criminal calling"
                              " himself the Joker (Heath Ledger) suddenly"
                              " throws the town into chaos,"
                              " the caped Crusader begins to tread a fine"
                              " line between heroism and vigilantism.",
                              "https://upload.wikimedia.org/wikipedia/en/th"
                              "umb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                              "July 14, 2008",
                              "Christian Bale",
                              "Heath Ledger")

# Movie Class Constructor for Inception Movie
inception = media.Movie("Inception",
                        "Dom Cobb (Leonardo DiCaprio) is a thief "
                        "with the rare ability to enter people's "
                        "dreams and steal their secrets from their "
                        "subconscious. His skill has made him a hot "
                        "commodity in the world of corporate espionage "
                        "but has also cost him everything he loves. "
                        "Cobb gets a chance at redemption when he is "
                        "offered a seemingly impossible task: Plant an "
                        "idea in someone's mind. If he succeeds, it "
                        "will be the perfect crime, but a dangerous "
                        "enemy anticipates Cobb's every move.",
                        "https://upload.wikimedia.org/wikipedia/en/th"
                        "umb/7/7f/Inception_ver3.jpg/220px-Inception_"
                        "ver3.jpg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4",
                        "July 8, 2010",
                        "Leonardo Di Caprio",
                        "Ellen Page")

# Movie Class Constructor for The Cone Collector Movie
the_bone_collector = media.Movie("The Bone Collector",
                                 "Policewoman Amelia Donaghy (Angelina Jolie)"
                                 "is in hot pursuit of a serial murderer "
                                 "whose calling card is a small shard of "
                                 "bone extracted from each of his victims. "
                                 "Unable to decipher the cryptic clues the "
                                 "killer leaves behind at the scene of the "
                                 "crime, Amelia calls upon quadriplegic "
                                 "forensic criminology expert Lincoln Rhyme "
                                 "(Denzel Washington) to help. With Amelia "
                                 "acting as Rhyme's able-bodied go-between, "
                                 "the pair piece together disparate clues, "
                                 "hoping they will learn who the next victim "
                                 "is.",
                                 "https://upload.wikimedia.org/wikipedia/en/th"
                                 "umb/3/31/Bone_collector_poster.jpg/220px-Bon"
                                 "e_collector_poster.jpg",
                                 "https://www.youtube.com/watch?v=wdyHrAbMVmE",
                                 "November 2, 1999",
                                 "Angelina Jolie",
                                 "Denzel Washington")

# Movie Class Constructor for The Departed Movie
the_departed = media.Movie("The Departed",
                           "South Boston cop Billy Costigan (Leonardo "
                           "DiCaprio) goes under cover to infiltrate "
                           "the organization of gangland chief Frank "
                           "Costello (Jack Nicholson). As Billy gains "
                           "the mobster's trust, a career criminal "
                           "named Colin Sullivan (Matt Damon) "
                           "infiltrates the police department and "
                           "reports on its activities to his syndicate "
                           "bosses. When both organizations learn "
                           "they have a mole in their midst, Billy and"
                           "Colin must figure out each other's "
                           "identities to save their own lives.",
                           "https://upload.wikimedia.org/wikipedia/en/th"
                           "umb/5/50/Departed234.jpg/220px-Departed234.j"
                           "pg",
                           "https://www.youtube.com/watch?v=SGWvwjZ0eDc",
                           "September 26, 2006",
                           "Leonardo Di Caprio",
                           "Matt Damon")

# Movie Class Constructor for Argo Movie
argo = media.Movie("Argo",
                   "On Nov. 4, 1979, militants storm the "
                   "U.S. embassy in Tehran, Iran, taking "
                   "66 American hostages. Amid the chaos, "
                   "six Americans manage to slip away and "
                   "find refuge with the Canadian "
                   "ambassador. Knowing that it's just a "
                   "matter of time before the refugees "
                   "are found and likely executed, the "
                   "U.S. government calls on extractor "
                   "Tony Mendez (Ben Affleck) to rescue "
                   "them. Mendez's plan is to pose as a "
                   "Hollywood producer scouting locations "
                   "in Iran and train the refugees to act "
                   "as his film crew.",
                   "https://upload.wikimedia.org/wikipedia/en/th"
                   "umb/e/e1/Argo2012Poster.jpg/220px-Argo2012Po"
                   "ster.jpg",
                   "https://www.youtube.com/watch?v=w918Eh3fij0",
                   "October 4, 2012",
                   "Ben Affleck",
                   "Bryan Cranston")

# Movie Class Constructor for The Silence of The Lambs Movie
the_silence_of_the_lambs = media.Movie("The Silence of The Lambs",
                                       "A young F.B.I. cadet must confide "
                                       "in an incarcerated and manipulative "
                                       "killer to receive his help on "
                                       "catching another serial killer "
                                       "who skins his victims.",
                                       "https://upload.wikimedia.org/wikipedia"
                                       "/en/thumb/8/86/The_Silence_of_the_Lamb"
                                       "s_poster.jpg/220px-The_Silence_of_the_"
                                       "Lambs_poster.jpg",
                                       "https://www.youtube.com/watch?v=lQKs1"
                                       "69Sl0I",
                                       "February 14, 1991",
                                       "Anthony Hopkins",
                                       "Jodie Foster")

# Create movies list array to pass on to the open_movies_page function
movies = [the_dark_knight, inception, the_bone_collector,
          the_departed, argo, the_silence_of_the_lambs]

# Pass on movies list to open_movies_page function
fresh_tomatoes.open_movies_page(movies)
