import matplotlib.pyplot as plt
def collatz_conjecture(n):
    """
    验证考拉兹猜想
    返回: 计算过程的列表
    """
    if n<= 0:
        raise ValueError('请输入正整数')
    sequence=[n]# 存储计算序列
    steps=0# 记录步数
    print(f'开始验证考拉兹猜想，初始值: {n}')
    while n!= 1:
        t=n
        if n%2==0:  # 如果是偶数
            n=n//2
            operation='÷2'
        else:  # 如果是奇数
            n=n*3+1
            operation='×3+1'
        sequence.append(n)
        steps+=1
        print(f'第{steps}步:{t}{operation}={n}')
    print(f'验证完成！经过 {steps} 步计算，最终结果为 1')
    print(f'计算序列: {sequence}')
    print(f'序列中元素的数量:{steps+1}')
    print(f'序列中最后三个数字:{sequence[-3]},{sequence[-2]},{sequence[-1]}')
    return sequence,steps


def plot_n7_line_chart():
    """
    绘制n=7的考拉兹序列折线图
    """
    n = 7
    sequence, steps = collatz_conjecture(n)
    # 创建步数序列
    step_numbers = list(range(len(sequence)))
    # 绘制折线图
    plt.figure(figsize=(10, 6))
    plt.plot(step_numbers, sequence, 'bo-', linewidth=2, markersize=6)
    plt.title(f'考拉兹猜想序列 (n={n})', fontsize=14)
    plt.xlabel('步数', fontsize=12)
    plt.ylabel('数值', fontsize=12)
    plt.grid(True, alpha=0.3)
    # 标记关键点
    plt.annotate(f'起点: {sequence[0]}', (0, sequence[0]), xytext=(10, 10),
                 textcoords='offset points', fontsize=10, color='red')
    plt.annotate(f'终点: {sequence[-1]}', (len(sequence) - 1, sequence[-1]),
                 xytext=(-30, 10), textcoords='offset points', fontsize=10, color='green')
    plt.tight_layout()
    plt.show()


def plot_n27_chart():
    """
    绘制n=27的考拉兹序列折线图
    """
    n = 27
    sequence, steps = collatz_conjecture(n)

    # 创建步数序列
    step_numbers = list(range(len(sequence)))

    # 绘制折线图
    plt.figure(figsize=(10, 6))
    plt.plot(step_numbers, sequence, 'ro-', linewidth=1.5, markersize=4)
    plt.title(f'考拉兹猜想序列 (n={n})', fontsize=14)
    plt.xlabel('步数', fontsize=12)
    plt.ylabel('数值', fontsize=12)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()
def get_user_numbers():
    """
    获取用户输入的数字，如果没输入则提示重新输入
    """
    while True:
        user_input=input('请输入想测试的数字（可以输入单个数字或多个数字，用空格或逗号分隔,输入q或Q可以退出程序）: ')
        print('-'*40)
        if user_input.strip() == "":
            print("您没有输入任何内容，请重新输入！")
            continue
        # 检查是否要退出程序
        if user_input.strip().lower() == 'q':
            return None
        # 处理用户输入的数字
        # 替换逗号为空格，然后分割
        cleaned_input=user_input.replace(',', ' ').replace('，', ' ')
        number_strings=cleaned_input.split()
        test_numbers=[]
        invalid_inputs=[]
        for num_str in number_strings:
            try:
                num=int(num_str)
                if num>0:
                    test_numbers.append(num)
                else:
                    invalid_inputs.append(f"'{num_str}'（非正整数）")
            except ValueError:
                invalid_inputs.append(f"'{num_str}'（非数字）")
        # 显示无效输入警告
        if invalid_inputs:
            print(f"警告: 跳过无效输入: {','.join(invalid_inputs)}")
        if test_numbers:
            return test_numbers
        else:
            print("没有有效的数字输入，请重新输入！")
# 主程序
if __name__=='__main__':
    print("**考拉兹猜想验证程序**")
    print("首先绘制n=7的考拉兹序列折线图：")
    plot_n7_line_chart()
    print("绘制n=27的考拉兹序列折线图：")
    plot_n27_chart()
    print("\n现在可以测试其他数字：")
    try:
        while True:
            # 获取用户输入的数字
            test_numbers=get_user_numbers()
            # 如果用户输入了q，退出程序
            if test_numbers is None:
                print("感谢使用，再见！")
                break
            print(f"将测试以下数字:{test_numbers}")
            # 测试用户输入的数字
            for num in test_numbers:
                collatz_conjecture(num)
            print("继续测试其他数字，或输入 'q' 退出程序")
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"发生错误: {e}")