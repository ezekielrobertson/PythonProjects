#ranked choice voting simulator thing
#needs some way to process things to vote on, 
#how many votes and in what way they are ranked, and how to generate a winner, deal with ties, etc.

from collections import defaultdict

#ballot will be received from parsing through the google sheets with the data collection
def ranked_choice_voting(ballots):
    vote_count = defaultdict(int)
    while True:
        #this will count the current round's votes
        for ballot in ballots:
            if ballot:
                vote_count[ballot[0]]+=1
        for candidate, count in vote_count.items():
            if count > len(ballots)/2: 
                #len(ballots)/2 will return a majority of the choices, i.e. 3/5, 5/7, etc.
                #this is the winner if they reach a majority of of the vote count
                return candidate
        #now is the time to elimnate the person with the least amount of votes 
        min_votes = min(vote_count.values())
        candidate_to_eliminate = [candidate for candidate, count in vote_count.items() if count == min_votes]
        if len(candidate_to_eliminate) == len(vote_count):
            return None
        for candidate in candidate_to_eliminate:
            del vote_count[candidate]
        #now to update the ballots after elimination of one of the candidates
        for i in range(len(ballots)):
            updated_ballot = []
            for candidate in ballots[i]:
                if candidate not in candidate_to_eliminate:
                    updated_ballot.append(candidate)
            ballots[i] = updated_ballot
        #clear the vote count for the second round
        vote_count.clear()
        #once we're down to one candidate, we have a winner 
        if len(vote_count) == 1:
            return list[vote_count.keys()[0]]

ballots = [
    ["Candidate A", "Candidate B", "Candidate C"],
    ["Candidate B", "Candidate C", "Candidate A"],
    ["Candidate C", "Candidate A", "Candidate B"],
    ["Candidate A", "Candidate B", "Candidate C"],
    ["Candidate B", "Candidate A", "Candidate C"],
]

print(ranked_choice_voting(ballots))