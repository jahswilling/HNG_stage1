from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000","http://localhost","https://cors-test.codehappy.dev"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


@app.get("/")
async def index():
    return { "slackUsername": "Javi", 
            "backend": True, "age": 26, 
            "bio": "Hi, I am jahswill Ovedhe  a self-motivated software engineer , "+
            "with extensive knowledge in building and implementing new solutions to solve real-world challenges."+
            " My programming career started with java mobile development and later with the flutter framework, "+
            "but I eventually became interested in web development with Python and its frameworks. "+
            "I've worked professionally as a full-stack developer for the last four years, though my primary strength is on the backend."+
            " I've worked on a couple of projects both independently and collaboratively"+
            "In my current position, I worked on some projects that necessitated the use of cloud-based infrastructure. "+
            "This piqued my interest in cloud computing and cloud development. Last year, I took learning more about the cloud seriously and passed the AWS cloud practitioner exam."+
            " To gain more professional experience, I recently completed the Udacity cloud developer nano-degree program. "+
            "I've worked with cloud infrastructure for the past year to build serverless apps, and microservices and am well-versed in various cloud technologies such as S3, SNS, CloudFront, lambda, dynamo, API gateway, ELB, and others."
            }