class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # burger --> sandwich --> bread


        # topological ordering
        # find out nodes with indegree of zero
        # decrement the incoming nodes
        # keep on doing this until no more nodes of indegree remaining

        # nodes are either ingredients or recipes
        # supplies are the nodes which you can make from 'scratch'

        from collections import deque
        q = deque(supplies)
        
        from collections import defaultdict
        ingredients_to_recipes = defaultdict(set)
        recipes_to_ingredients = defaultdict(set)
        for recipe, req_ingredients in zip(recipes,ingredients):
            for ing in req_ingredients:
                ingredients_to_recipes[ing].add(recipe)
            recipes_to_ingredients[recipe] = set(req_ingredients)
        
        recipes_created = []
        while q:
            ingredient = q.popleft()
            print(ingredient)
            # remove ing from all recipes that 'require' this ingredient
            eligible_recipes = ingredients_to_recipes[ingredient]
            for recipe in eligible_recipes:
                recipes_to_ingredients[recipe].remove(ingredient)
                if len(recipes_to_ingredients[recipe]) == 0:
                    recipes_created.append(recipe)
                    q.append(recipe)
        return recipes_created


