from pydantic import BaseModel


class User(BaseModel):
    name: str
    username: str
    twitter_username: str
    github_username: str
    website_url: str
    profile_image: str
    profile_image_90: str


class Organization(BaseModel):
    name: str
    username: str
    slug: str
    profile_image: str
    profile_image_90: str


class Article(BaseModel):
    type_of: str
    id: int
    title: str
    description: str
    cover_image: str
    readable_publish_date: str
    social_image: str
    tag_list: str
    tags: list[str]
    slug: str
    path: str
    url: str
    canonical_url: str
    comments_count: int
    positive_reactions_count: int
    public_reactions_count: int
    collection_id: int
    created_at: str
    edited_at: str
    crossposted_at: str
    published_at: str
    last_comment_at: str
    published_timestamp: str
    reading_time_minutes: int
    body_html: str
    body_markdown: str
    user: User
    organization: Organization


"""{
  "type_of": "article",
  "id": 150589,
  "title": "Byte Sized Episode 2: The Creation of Graph Theory ",
  "description": "The full story of Leonhard Euler and the creation of this fundamental computer science principle, delivered in a few minutes.",
  "cover_image": "https://res.cloudinary.com/practicaldev/image/fetch/s--qgutBUrH--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://thepracticaldev.s3.amazonaws.com/i/88e62fzblbluz1dm7xjf.png",
  "readable_publish_date": "Aug  1",
  "social_image": "https://res.cloudinary.com/practicaldev/image/fetch/s--6wSHHfwd--/c_imagga_scale,f_auto,fl_progressive,h_500,q_auto,w_1000/https://thepracticaldev.s3.amazonaws.com/i/88e62fzblbluz1dm7xjf.png",
  "tag_list": "computerscience, graphtheory, bytesized, history",
  "tags": [
    "computerscience",
    "graphtheory",
    "bytesized",
    "history"
  ],
  "slug": "byte-sized-episode-2-the-creation-of-graph-theory-34g1",
  "path": "/bytesized/byte-sized-episode-2-the-creation-of-graph-theory-34g1",
  "url": "https://dev.to/bytesized/byte-sized-episode-2-the-creation-of-graph-theory-34g1",
  "canonical_url": "https://dev.to/bytesized/byte-sized-episode-2-the-creation-of-graph-theory-34g1",
  "comments_count": 21,
  "positive_reactions_count": 122,
  "public_reactions_count": 322,
  "collection_id": 1693,
  "created_at": "2019-07-31T11:15:06Z",
  "edited_at": null,
  "crossposted_at": null,
  "published_at": "2019-08-01T15:47:54Z",
  "last_comment_at": "2019-08-06T16:48:10Z",
  "published_timestamp": "2019-08-01T15:47:54Z",
  "reading_time_minutes": 15,
  "body_html": "<p>Today's episode of Byte Sized is about Leonhard Euler and the creation of <a href=\"https://en.wikipedia.org/wiki/Graph_theory\">Graph Theory</a>.</p>\n\n<p>For more about how Graph Theory works, check out this video from BaseCS!</p>...\n",
  "body_markdown": "---\r\ntitle: Byte Sized Episode 2: The Creation of Graph Theory \r\npublished: true\r\ndescription: The full story of Leonhard Euler and the creation of this fundamental computer science principle, delivered in a few minutes.\r\ntags: computerscience, graphtheory, bytesized, history\r\ncover_image: https://thepracticaldev.s3.amazonaws.com/i/88e62fzblbluz1dm7xjf.png\r\nseries: Byte Sized Season 1\r\n---\r\n\r\nToday's episode of Byte Sized is about Leonhard Euler and the creation of [Graph Theory](https://en.wikipedia.org/wiki/Graph_theory).\r\n\r\nFor more about how Graph Theory works, check out this video from BaseCS!...",
  "user": {
    "name": "Vaidehi Joshi",
    "username": "vaidehijoshi",
    "twitter_username": "vaidehijoshi",
    "github_username": "vaidehijoshi",
    "website_url": "http://www.vaidehi.com",
    "profile_image": "https://res.cloudinary.com/practicaldev/image/fetch/s--eDGAYAoK--/c_fill,f_auto,fl_progressive,h_640,q_auto,w_640/https://thepracticaldev.s3.amazonaws.com/uploads/user/profile_image/2882/K2evUksb.jpg",
    "profile_image_90": "https://res.cloudinary.com/practicaldev/image/fetch/s--htZnqMn3--/c_fill,f_auto,fl_progressive,h_90,q_auto,w_90/https://thepracticaldev.s3.amazonaws.com/uploads/user/profile_image/2882/K2evUksb.jpg"
  },
  "organization": {
    "name": "Byte Sized",
    "username": "bytesized",
    "slug": "bytesized",
    "profile_image": "https://res.cloudinary.com/practicaldev/image/fetch/s--sq0DrZfn--/c_fill,f_auto,fl_progressive,h_640,q_auto,w_640/https://thepracticaldev.s3.amazonaws.com/uploads/organization/profile_image/865/652f7998-32a8-4fd9-85ca-dd697d2a9ee9.png",
    "profile_image_90": "https://res.cloudinary.com/practicaldev/image/fetch/s--1Pt_ICL---/c_fill,f_auto,fl_progressive,h_90,q_auto,w_90/https://thepracticaldev.s3.amazonaws.com/uploads/organization/profile_image/865/652f7998-32a8-4fd9-85ca-dd697d2a9ee9.png"
  }
}"""
