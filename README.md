#AllReviewInterface
This is a simple web service that allows a number of student reviews to be sent to various other web services and their results collected in an easy-to-parse form. The purpose of this is to make it easier to run student reviews against various review web services simultaneously.

That being said, the primary purpose for the creation of this web service is to serve as a copyable template for future web services created for the PeerLogic web server. This README similarly serves as a template for a proper README for such services.

Note that no more than 10 reviews should be passed in at a time for performance considerations, if possible.

#URL Path
This service can be reached at peerlogic.csc.ncsu.edu/allreviewinterface/call_models. It is set up on port 3013 of the PeerLogic web server. (Note that all services MUST have unique ports).

#Input
This service expects a GET request with the following JSON payload format:
{
	"services": the names of the PeerLogic web services to call. The following are currently supported:
		-intelligent_assignment_volume (measures the length and word count of the reviews)
		-intelligent_assignment_problems (determines whether the review mentioned the work having problems)
		-intelligent_assignment_suggestions (determines whether the review had suggestions)
	
	"input": contains the input JSON to be passed to the review services. This web service assumes all services called can use the same input format, which is true for the currently supported services. This JSON component contains:
	{
		"reviews": a list of the review objects to have NLP applied to. That list contains items of the following format:
			[
			"id": the id number of the review. Should be unique between given reviews.
			"text": the text of the review itself.
			]
			
	}
# Example Input
{ "services" : ["intelligent_assignment_volume","intelligent_assignment_problems"],
	
	"input" : 
 { "reviews" : [
      {
      "id" : 1,
      "text" : "This is incredible! I can't find a single thing wrong with your project! This is simply great, you are amazing, great job! Only thing I can say is I might have made the font size larger."
  },
      {
          "id" : 2,
          "text" : "I think your project is poorly put together and is missing most of the project requirements."
      },
	    {
          "id" : 3,
          "text" : "It was good."
      }
  ]
  }
}

# Example Output