import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
						"a story of a boy and his toys that come to life",
						"https://imgsa.baidu.com/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=4b38e0e5bca1cd1111bb7a72d87ba399/0e2442a7d933c89562a79caed71373f08302000d.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print (toy_story.storyline)
avatar = media.Movie("avatar",
					"a marine on the alient planet",
					"https://imgsa.baidu.com/baike/c0%3Dbaike220%2C5%2C5%2C220%2C73/sign=8983a693612762d09433acedc185639f/eaf81a4c510fd9f9f7454cd9272dd42a2834a42b.jpg",
					"https://www.youtube.com/watch?v=d1_JBMrrYw8")
# print (avatar.storyline)
# avatar.show_trailer()
school_rock = media.Movie("school_rock",
						 "use the rock music to learn",
						 "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
						 "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# movies = [toy_story, avatar, school_rock]
# fresh_tomatoes.open_movies_page(movies)
# media.Movie.CLASS_VARIABLE = media.Movie.CLASS_VARIABLE + 1
# print(media.Movie.CLASS_VARIABLE)
print(media.Movie.__module__)