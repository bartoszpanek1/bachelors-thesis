class ResponseThresholds:
    def __init__(self, min_pos, max_pos, min_bel, max_bel, min_know, max_know):
        self.min_pos = min_pos
        self.max_pos = max_pos
        self.min_bel = min_bel
        self.max_bel = max_bel
        self.min_know = min_know
        self.max_know = max_know

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
