import spacy

nlp = spacy.load("en_core_web_lg")

def replace_less_detailed_sentences(overall_summary, highlighted_summary, similarity_threshold = 0.6):
    for paraphrased_sentence in highlighted_summary:
        similarity_scores = [nlp(paraphrased_sentence).similarity(nlp(sentence)) for sentence in overall_summary]

        max_similarity_index = similarity_scores.index(max(similarity_scores))

        if max(similarity_scores) > similarity_threshold:
            overall_summary[max_similarity_index] = paraphrased_sentence

    return overall_summary

# new_summary = replace_less_detailed_sentences(overall_summary, highlighted_sections)