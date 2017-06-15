![Perspective](p_logo.png)

# The Perspective Initiative

This repository is for the work done with Perspective API.

@uthor: Haji Mohammad Saleem

## Initial Report

### Comparative analysis of the Perspective API and community-based classification system on Reddit comments

#### Abstract

In our previous work, we developed a community-based classification system that used the comments in self-identifying hateful communities to train target-specific hate speech classifiers. In this analysis, we compare the performance of our classification system against that of the Perspective API, on a set of Reddit comments. We find that of toxicity (as operationalized in the Perspective API) and hate speech, are similar yet distinct concepts. The two systems surface different behaviors and combined results of the two can increase the quality of our community-based silver-standard hate speech dataset.

[PDF](docs/Report.pdf)

## Follow-up Work

- [ ] Get the median score of Perspective results.
- [ ] Run the Perspective API on three support subreddits.
- [ ] Run the Perspective API on three random subreddits.
- [ ] Run the classifiers on Perspective Data.
- [ ] Generate ROC curves from classifier results.
