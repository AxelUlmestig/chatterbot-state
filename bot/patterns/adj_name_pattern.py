import bot.pattern_tools as pt

def match_pattern(tree):
	adjective = pt.find_node(tree, pt.match_POS("JJ"))
	name = pt.find_node(adjective, pt.match_POS("NNP"))
	if name and adjective:
		return {"name": name.word, "adjective": adjective.word, "negation": adjective.is_negated()}
	else:
		return None

def execute_action(knowledge, name, adjective, negation):
	if negation:
		knowledge.remove_personal_info(name, adjective)
	else:
		knowledge.add_personal_info(name, adjective)
	response = "I see."
	return response

pattern = pt.create_pattern(execute_action, match_pattern)
