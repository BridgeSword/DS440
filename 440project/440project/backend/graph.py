import networkx as nx
import matplotlib.pyplot as plt

# 创建PERT图
G = nx.DiGraph()

# 添加节点，表示项目的活动
activities = {
    '1': "Project Start",
    '2': "Research & Analysis (3 days)",
    '3': "Requirement Gathering (4 days)",
    '4': "Initial Design (2 days)",
    '5': "Backend Development (7 days)",
    '6': "Frontend Development (6 days)",
    '7': "Data Preprocessing (3 days)",
    '8': "Model Development (5 days)",
    '9': "Model Optimization (3 days)",
    '10': "Integration (2 days)",
    '11': "System Testing (4 days)",
    '12': "Bug Fixing (3 days)",
    '13': "Deployment (2 days)",
    '14': "User Acceptance Testing (2 days)",
    '15': "Documentation (1 day)",
    '16': "Project End"
}

# 添加节点到图中
for node, label in activities.items():
    G.add_node(node, label=label)

# 定义边及其时间成本
edges = [
    ('1', '2', '3 days'),
    ('2', '3', '4 days'),
    ('3', '4', '2 days'),
    ('4', '5', '7 days'),
    ('4', '6', '6 days'),
    ('1', '7', '3 days'),
    ('7', '8', '5 days'),
    ('8', '9', '3 days'),
    ('9', '10', '2 days'),
    ('5', '10', '1 day'),
    ('6', '10', '1 day'),
    ('10', '11', '4 days'),
    ('11', '12', '3 days'),
    ('12', '13', '2 days'),
    ('13', '14', '2 days'),
    ('14', '15', '1 day'),
    ('15', '16', '0 days')
]

# 将边加入到图中，并标记时间成本
for src, dst, duration in edges:
    G.add_edge(src, dst, label=duration)

# 设置布局
pos = nx.spring_layout(G, seed=42)

# 绘制节点
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_weight='bold')

# 绘制边的标签（持续时间）
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("PERT Chart for Project Timeline")
plt.tight_layout()
plt.savefig("C:\\Users\\BridgeSword\\Desktop\\PERT_Chart.png")
plt.show()
