# UC3M/COMPASS compatibility problems and notes
* UC3M doesn't have a description field. We're using qualification field.
* Translate automatically from the UC3M free text fields to COMPASS fixed vocabularies is not a trivial task, would need more complex processing in order to achieve it (NLP) (competence, objective, subject).

Because of compatibility  problems or non existence in UC3M, there are fields not implemented yet:
* Rights
* Subject
* Relation
* Qualification
* Prerequisite
* Objective
* HasPart

# Some notes
* Doesn't make sense the credits of the course are not a fixed vocabulary, usually are "ECTS" if not they can be added later to the COMPASS vocabulary. It would make easier to search courses by credits (time to expend in the course), more complex search (like "same ECTS and same competence"), or even define the equivalence between different credits specifications building a more powerful system (1 "ECTS" eq. 0.5 "UC3M imaginary credits").
