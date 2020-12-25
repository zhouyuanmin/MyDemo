def call_counter(func):
    limit_call = 10

    def helper(x):
        if helper.calls >= limit_call:
            raise AssertionError(f"单个程序最多允许调用此方法{limit_call}次")
        helper.calls += 1
        return func(x)

    helper.calls = 0
    return helper


@call_counter
def succ(x):
    return x + 1


if __name__ == '__main__':
    print(succ.calls)
    for i in range(12):
        print(succ(i))
    print(succ.calls)
