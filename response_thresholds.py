class ResponseThresholds:
    def __init__(self):
        self.min_pos = 0
        self.max_pos = 0.66
        self.min_bel = 0.66
        self.max_bel = 1
        self.min_know = 1
        self.max_know = 1

    def get_response(self, probability, all_data_taken):
        if probability == self.max_know:
            if all_data_taken:
                return 'Know'
            else:
                return 'Bel'
        elif self.min_bel < probability < self.max_bel:
            return 'Bel'
        elif self.min_pos <= probability <= self.max_pos:
            return 'Pos'