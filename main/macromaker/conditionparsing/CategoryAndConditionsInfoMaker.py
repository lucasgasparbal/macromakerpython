class CategoryAndConditionsInfoMaker:

    def categoryAndConditionsInfo(self,category,conditions):
        conditionsInfo = []
        for condition in conditions:
            conditionsInfo.append(condition.getConditionHelpInfo())

        return {category: conditionsInfo}
