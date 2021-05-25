'''
parse a 10G log file and print which host had how many percentage of 5XX

'''
import click

from concurrent.futures import ThreadPoolExecutor, as_completed


@click.command()
@click.option('--file', help="Log file path. Can add multiple files", required=True, multiple=True)
@click.option('--start', help="Consider logs after this time (inclusive). Format is epoch milliseconds", required=True)
@click.option('--end', help="Consider logs before this time (exclusive). Format is epoch milliseconds", required=True)
def count_5xx(file, start, end):
    list_files = file
    start = int(start)
    end = int(end)

    # Thread safe
    # ref: https://docs.python.org/3/glossary.html#term-global-interpreter-lock
    counts = dict()
    errors = dict()

    def parse_one_file(file_path):
        with open(file_path) as f:
            for line in f:
                l = line.split(" | ")  # can be optmized further by not splitting whole line but only take out relevant parts

                # ASSUMING all lines are in expected formatted. Else handle out of index and other kinds of errors
                status_code = l[4]
                time_ms = float(l[0])*1000
                host = l[2]

                if time_ms >= start and time_ms < end:
                    counts[host] = counts.get(host, 0) + 1
                    if status_code.startswith("5"):
                        errors[host] = errors.get(host, 0) + 1

    # size of pool is equal to number of files
    # makes more sense to cap it at disk io limit. Beyond that, larger pool will result into slower times
    with ThreadPoolExecutor(len(list_files)) as t:
        future_to_file = {t.submit(parse_one_file, f): f for f in list_files}
        for future in as_completed(future_to_file):
            file_path = future_to_file[future]
            try:
                # this call will ensure we get exception raised here if the function resulted in exception
                future.result()
            except Exception as exc:
                print(f"Could not parse file {file_path}. Exception: {exc}")

    print(f"\n\nBetween time {start} and {end}")
    error_lines = [f"{host} returned {errors[host]/counts[host]*100}% of 5xx errors" for host in errors]
    if not error_lines:
        error_lines = ["No host saw 5xx"]
    print("\n".join(error_lines))
    print("\n")


if __name__ == "__main__":
    count_5xx()