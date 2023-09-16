import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_lg")

def replace_less_detailed_sentences(overall_summary, highlighted_sections):
    # Initialize an empty result list
    result_summary = []

    # Loop through each paraphrased subsection
    for paraphrased_sentence in highlighted_sections:
        # Calculate similarity scores between the paraphrased sentence and sentences in the overall summary
        similarity_scores = [nlp(paraphrased_sentence).similarity(nlp(sentence)) for sentence in overall_summary]

        # Find the index of the sentence in the overall summary with the highest similarity score
        max_similarity_index = similarity_scores.index(max(similarity_scores))

        # Replace the sentence in the overall summary with the paraphrased subsection
        overall_summary[max_similarity_index] = paraphrased_sentence

    return overall_summary

# new_summary = replace_less_detailed_sentences(overall_summary, highlighted_sections)