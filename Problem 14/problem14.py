chain_lengths = {}


def get_chain_length(seed: int) -> int:
    chain_length = 1
    current_value = seed
    while current_value > 1:
        seed_length = chain_lengths.get(current_value)
        if seed_length:
            chain_length = seed_length + chain_length - 1
            break
        if current_value % 2 == 0:
            current_value >>= 1
        else:
            current_value = 3*current_value + 1
        chain_length += 1
    chain_lengths[seed] = chain_length
    return chain_length


def calculate_max_chain(max_candidate_seed: int) -> int:
    max_chain_length = 0
    max_chain_seed = 2
    seed = 2
    while seed < max_candidate_seed:
        chain_length = get_chain_length(seed)
        if chain_length > max_chain_length:
            max_chain_length = chain_length
            max_chain_seed = seed
        seed += 1
    return max_chain_seed


MAX_CANDIDATE_SEED = 1000000

# Max chain for seed less than 1000000 is 525 using seed 837799
max_seed = calculate_max_chain(MAX_CANDIDATE_SEED)
print("Max chain for seed less than " + str(MAX_CANDIDATE_SEED) + " is "
      + str(get_chain_length(max_seed)) + " using seed " + str(max_seed))
