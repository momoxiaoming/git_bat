import os
import winreg


def add_env_var(name, value):
    """
    在Windows系统中添加环境变量
    """
    try:
        # 获取系统环境变量表的键
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
                             0, winreg.KEY_ALL_ACCESS)

        # 检查环境变量是否存在
        env_vars = winreg.QueryValueEx(key, 'Path')[0]
        if value in env_vars:
            print(f'{value} already exists in environment variables.')
            return

        # 添加环境变量
        env_vars = f'{env_vars};{value}'
        winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, env_vars)
        os.environ['Path'] = env_vars

        print(f'{value} has been added to environment variables.')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    # 示例：添加Python解释器的环境变量
    os.chdir('../')
    python38=os.getcwd()+"\\tools\\python3.8"
    jdk11=os.getcwd()+"\\tools\\jdk11\\jre\\bin"
    obs=os.getcwd()+"\\tools\\obs-gen-210512\\win"
    git=os.getcwd()+"\\tools\\Git\\bin"

    add_env_var('python38', python38)
    add_env_var('jdk11', jdk11)
    add_env_var('obs', obs)
    add_env_var('git', git)
