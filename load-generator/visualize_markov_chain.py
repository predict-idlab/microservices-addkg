from tasks import MarkovChain, Index

if __name__ == '__main__':
    from utils import plot_g_pyviz

    task_chain = MarkovChain(root=Index)
    plot_g_pyviz(task_chain)
