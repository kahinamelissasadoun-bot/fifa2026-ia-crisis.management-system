"""
FIFA World Cup 2026 - Multi-Agent Crisis Management System
Professional AI Dashboard with Advanced Communication Network Visualization
Developed by SADOUN Kahina Melissa & BENDAIKHA Meriem
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import networkx as nx
from datetime import datetime
import json
import base64

st.set_page_config(
    page_title="FIFA 2026 AI Crisis Manager",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: #f5f5f5;
        padding: 0;
    }
    
    .stApp {
        background: #f5f5f5;
    }
    
    .header-container {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 2.5rem 3rem;
        border-radius: 0 0 30px 30px;
        margin-bottom: 2rem;
        box-shadow: 0 15px 50px rgba(0,0,0,0.5);
        position: relative;
        overflow: hidden;
    }
    
    .header-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #00d4ff 0%, #0099ff 50%, #0066cc 100%);
    }
    
    .header-title {
        color: #ffffff;
        font-size: 3rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: 0.5px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
    }
    
    .header-subtitle {
        color: #00d4ff;
        font-size: 1.2rem;
        margin-top: 0.8rem;
        font-weight: 400;
        letter-spacing: 1px;
    }
    
    .logo-container {
        display: flex;
        gap: 2rem;
        align-items: center;
    }
    
    .logo-enp {
        width: 100px;
        height: auto;
        filter: brightness(1.2);
    }
    
    .logo-fifa {
        width: 90px;
        height: auto;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 1.8rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 2px solid #00d4ff;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #00d4ff 0%, #0099ff 100%);
    }
    
    .metric-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0, 212, 255, 0.3);
        border-color: #0099ff;
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 800;
        color: #0066cc !important;
    }
    
    div[data-testid="stMetricLabel"] {
        font-size: 0.95rem;
        color: #495057 !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 600;
    }
    
    div[data-testid="stMetricDelta"] {
        color: #28a745 !important;
        font-weight: 700;
    }
    
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a1a2e;
        margin-top: 3rem;
        margin-bottom: 1.5rem;
        padding: 1rem 1.5rem;
        background: linear-gradient(135deg, #ffffff 0%, #f0f0f0 100%);
        border-radius: 12px;
        border-left: 5px solid #00d4ff;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #00d4ff 0%, #0099ff 100%);
        color: #ffffff;
        font-weight: 700;
        border: none;
        padding: 1rem 2rem;
        border-radius: 12px;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(0, 153, 255, 0.4);
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.6);
        background: linear-gradient(135deg, #0099ff 0%, #0066cc 100%);
    }
    
    .timeline-item {
        padding: 1.5rem;
        border-left: 4px solid #00d4ff;
        margin-left: 1.5rem;
        margin-bottom: 1.5rem;
        background: #ffffff;
        border-radius: 0 12px 12px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        color: #333333;
        transition: all 0.3s ease;
    }
    
    .timeline-item:hover {
        transform: translateX(10px);
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.2);
    }
    
    .message-log {
        background: #ffffff;
        color: #333333;
        padding: 1.5rem;
        border-radius: 12px;
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
        max-height: 450px;
        overflow-y: auto;
        margin-bottom: 1.5rem;
        border: 2px solid #e0e0e0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    
    .message-line {
        padding: 0.5rem;
        border-bottom: 1px solid #e0e0e0;
        transition: background 0.2s ease;
    }
    
    .message-line:hover {
        background: rgba(0, 212, 255, 0.1);
    }
    
    .message-request {
        color: #f59e0b;
    }
    
    .message-response {
        color: #10b981;
    }
    
    .message-transfer {
        color: #0099ff;
    }
    
    .message-alert {
        color: #ef4444;
    }
    
    .agent-status-card {
        background: #ffffff;
        padding: 1.2rem;
        border-radius: 12px;
        border: 2px solid #e0e0e0;
        margin-bottom: 1rem;
        color: #333333;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    .agent-status-card:hover {
        border-color: #00d4ff;
        box-shadow: 0 6px 20px rgba(0, 212, 255, 0.2);
    }
    
    .badge-active {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 3px 10px rgba(16, 185, 129, 0.4);
    }
    
    .badge-inactive {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 3px 10px rgba(239, 68, 68, 0.4);
    }
    
    .communication-stats {
        background: linear-gradient(135deg, #00d4ff 0%, #0099ff 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0, 153, 255, 0.4);
    }
    
    .stExpander {
        background: #ffffff;
        border-radius: 12px;
        border: 2px solid #e0e0e0;
        margin-bottom: 1rem;
    }
    
    div[data-testid="stExpander"] {
        background: #ffffff;
        border: 2px solid #e0e0e0;
    }
    
    .sidebar .sidebar-content {
        background: #ffffff;
    }
    
    section[data-testid="stSidebar"] {
        background: #ffffff;
    }
    
    section[data-testid="stSidebar"] > div {
        background: #ffffff;
    }
    
    .stDataFrame {
        background: #ffffff;
        border-radius: 12px;
        overflow: hidden;
    }
    
    .footer-container {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        padding: 2.5rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 3rem;
        border-top: 3px solid #00d4ff;
        box-shadow: 0 -5px 20px rgba(0,0,0,0.2);
    }
    
    .footer-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #00d4ff;
        margin-bottom: 1rem;
        letter-spacing: 1px;
    }
    
    .footer-authors {
        font-size: 1.1rem;
        color: #ffffff;
        font-weight: 600;
        margin: 0.8rem 0;
    }
    
    .footer-subtitle {
        font-size: 0.95rem;
        color: #b8d4e8;
        margin-top: 0.5rem;
    }
    
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #00d4ff 0%, #0099ff 100%);
    }
    
    label {
        color: #333333 !important;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

class Message:
    def __init__(self, msg_type, sender, receiver, content, timestamp):
        self.type = msg_type
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = timestamp

class EnvironmentHybrid:
    def __init__(self, cities_data):
        self.cities = list(cities_data.keys())
        self.dynamic_state = {}
        self.messages_log = []
        
        for city, data in cities_data.items():
            self.dynamic_state[city] = {
                'occupancy_rate': data['occupancy'],
                'crisis_level': 0.0,
                'available_rooms': data['capacity'],
                'stress_level': 'BAS',
                'resources_received': 0,
                'resources_given': 0,
                'cluster': data['cluster'],
                'popularity_rank': data['popularity'],
                'num_matches': data['matches'],
                'capacity': data['capacity'],
                'messages_sent': 0,
                'messages_received': 0
            }
    
    def log_message(self, msg):
        self.messages_log.append(msg)
    
    def get_city_state(self, city):
        occ = self.dynamic_state[city]['occupancy_rate']
        capacity = self.dynamic_state[city]['capacity']
        
        if occ >= 0.85:
            stress = 'CRITICAL'
            crisis = 0.9
        elif occ >= 0.70:
            stress = 'HIGH'
            crisis = 0.7
        elif occ >= 0.50:
            stress = 'MEDIUM'
            crisis = 0.4
        else:
            stress = 'LOW'
            crisis = 0.1
        
        self.dynamic_state[city]['stress_level'] = stress
        self.dynamic_state[city]['crisis_level'] = crisis
        self.dynamic_state[city]['available_rooms'] = int(capacity * (1 - occ))
        
        return {
            'city': city,
            'occupancy_rate': occ,
            'crisis_level': crisis,
            'available_rooms': self.dynamic_state[city]['available_rooms'],
            'stress_level': stress,
            'cluster': self.dynamic_state[city]['cluster'],
            'popularity_rank': self.dynamic_state[city]['popularity_rank'],
            'resources_received': self.dynamic_state[city]['resources_received'],
            'resources_given': self.dynamic_state[city]['resources_given'],
            'num_matches': self.dynamic_state[city]['num_matches'],
            'capacity': capacity,
            'messages_sent': self.dynamic_state[city]['messages_sent'],
            'messages_received': self.dynamic_state[city]['messages_received']
        }

class BayesianCrisisPredictor:
    def __init__(self):
        self.rules_applied = {}
    
    def predict_crisis_probability(self, city_state):
        occ = city_state['occupancy_rate']
        cluster_score = 0.60 if city_state['cluster'] == 0 else 0.40
        hadoop_score = 0.55 + (city_state['num_matches'] / 12) * 0.1
        crisis_prob = 0.60 * occ + 0.20 * hadoop_score + 0.20 * cluster_score
        return np.clip(crisis_prob, 0.0, 1.0)
    
    def classify_risk_ml(self, city_state):
        occ = city_state['occupancy_rate']
        if occ >= 0.75:
            return 'HIGH_RISK'
        elif occ >= 0.50:
            return 'MEDIUM_RISK'
        else:
            return 'LOW_RISK'
    
    def get_recommendations(self, city_state):
        crisis_prob = self.predict_crisis_probability(city_state)
        
        if crisis_prob >= 0.75:
            return "CRITICAL: Immediate coordinator intervention required"
        elif crisis_prob >= 0.60:
            return "HIGH RISK: Request assistance from helper cities"
        elif crisis_prob >= 0.45:
            return "MODERATE: Optimize local resources and monitor closely"
        else:
            return "STABLE: Resources available to assist other cities"

class AgentCoordinator:
    def __init__(self):
        self.interventions = 0
        self.crises_resolved = 0
        self.transfers_log = []
        self.decisions_log = []
        self.communication_graph = {'nodes': [], 'edges': []}
        self.messages_sent = 0
        self.messages_received = 0
    
    def detect_and_coordinate(self, env, bayesian):
        crises = []
        helpers = []
        
        for city in env.cities:
            state = env.get_city_state(city)
            crisis_prob = bayesian.predict_crisis_probability(state)
            
            msg = Message(
                'PERCEPTION',
                city,
                'Coordinator',
                f"Status report: Occ={state['occupancy_rate']:.2f}, Crisis={crisis_prob:.2f}",
                datetime.now()
            )
            env.log_message(msg)
            env.dynamic_state[city]['messages_sent'] += 1
            self.messages_received += 1
            
            if crisis_prob >= 0.68 or state['occupancy_rate'] >= 0.78:
                crises.append((city, crisis_prob, state['occupancy_rate']))
                
                alert_msg = Message(
                    'ALERT',
                    city,
                    'Coordinator',
                    f"CRISIS ALERT: Immediate assistance required",
                    datetime.now()
                )
                env.log_message(alert_msg)
                env.dynamic_state[city]['messages_sent'] += 1
                self.messages_received += 1
                
            elif crisis_prob < 0.52 and state['occupancy_rate'] < 0.60:
                helpers.append((city, state['available_rooms']))
                
                offer_msg = Message(
                    'OFFER',
                    city,
                    'Coordinator',
                    f"Available to help: {state['available_rooms']:,} rooms free",
                    datetime.now()
                )
                env.log_message(offer_msg)
                env.dynamic_state[city]['messages_sent'] += 1
                self.messages_received += 1
        
        if len(crises) > 0 and len(helpers) > 0:
            decision_msg = Message(
                'DECISION',
                'Coordinator',
                'ALL',
                f"Initiating coordination: {len(crises)} crises, {len(helpers)} helpers",
                datetime.now()
            )
            env.log_message(decision_msg)
            self.messages_sent += 1
            
            for crisis_city, crisis_prob, crisis_occ in crises[:2]:
                if helpers:
                    helper_city, helper_rooms = helpers[0]
                    reduction = 0.15 if len(crises) > 1 else 0.18
                    
                    request_msg = Message(
                        'REQUEST',
                        'Coordinator',
                        helper_city,
                        f"Transfer {reduction*100:.0f}% capacity to {crisis_city}",
                        datetime.now()
                    )
                    env.log_message(request_msg)
                    self.messages_sent += 1
                    env.dynamic_state[helper_city]['messages_received'] += 1
                    
                    self.transfer_resources(env, helper_city, crisis_city, reduction)
                    
                    confirm_msg = Message(
                        'TRANSFER',
                        helper_city,
                        crisis_city,
                        f"Resources transferred: {reduction*100:.0f}% capacity",
                        datetime.now()
                    )
                    env.log_message(confirm_msg)
                    env.dynamic_state[helper_city]['messages_sent'] += 1
                    env.dynamic_state[crisis_city]['messages_received'] += 1
                    
                    self.transfers_log.append({
                        'from': helper_city,
                        'to': crisis_city,
                        'reduction': reduction,
                        'crisis_prob': crisis_prob
                    })
                    self.interventions += 1
                    
                    self.communication_graph['edges'].append({
                        'from': helper_city,
                        'to': crisis_city,
                        'type': 'transfer',
                        'weight': reduction
                    })
            
            self.crises_resolved = len(crises)
        
        for city in env.cities:
            self.communication_graph['nodes'].append({
                'id': city,
                'type': 'agent',
                'status': env.get_city_state(city)['stress_level']
            })
        
        self.communication_graph['nodes'].append({
            'id': 'Coordinator',
            'type': 'coordinator',
            'status': 'ACTIVE'
        })
        
        for city in env.cities:
            self.communication_graph['edges'].append({
                'from': city,
                'to': 'Coordinator',
                'type': 'report',
                'weight': 1
            })
        
        return len(crises), len(helpers), crises, helpers
    
    def transfer_resources(self, env, from_city, to_city, reduction):
        current_occ = env.dynamic_state[to_city]['occupancy_rate']
        new_occ = max(0.30, current_occ - reduction)
        env.dynamic_state[to_city]['occupancy_rate'] = new_occ
        
        capacity = env.dynamic_state[to_city]['capacity']
        resources = int(capacity * reduction)
        env.dynamic_state[to_city]['resources_received'] += resources
        env.dynamic_state[from_city]['resources_given'] += resources

def calculate_system_score(env):
    total = 0
    for city in env.cities:
        state = env.get_city_state(city)
        occ = state['occupancy_rate']
        
        if 0.40 <= occ <= 0.65:
            occ_score = 12
        elif 0.30 <= occ <= 0.75:
            occ_score = 9
        else:
            occ_score = 5
        
        crisis_score = 10 if state['crisis_level'] < 0.30 else 7 if state['crisis_level'] < 0.60 else 3
        total += occ_score + crisis_score
    
    return int((total / (22 * len(env.cities))) * 100)

def create_agent_network_graph(coordinator, env):
    G = nx.DiGraph()
    
    G.add_node('Coordinator', node_type='coordinator')
    for city in env.cities:
        state = env.get_city_state(city)
        G.add_node(city, node_type='agent', stress=state['stress_level'])
    
    for edge in coordinator.communication_graph['edges']:
        G.add_edge(edge['from'], edge['to'], 
                  edge_type=edge['type'], 
                  weight=edge.get('weight', 1))
    
    pos = nx.spring_layout(G, k=2, iterations=50)
    
    edge_trace_report = []
    edge_trace_transfer = []
    
    for edge in G.edges(data=True):
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        
        edge_type = edge[2].get('edge_type', 'report')
        
        if edge_type == 'transfer':
            edge_trace_transfer.append(
                go.Scatter(
                    x=[x0, x1, None],
                    y=[y0, y1, None],
                    mode='lines',
                    line=dict(width=5, color='#00d4ff'),
                    hoverinfo='none',
                    showlegend=False
                )
            )
        else:
            edge_trace_report.append(
                go.Scatter(
                    x=[x0, x1, None],
                    y=[y0, y1, None],
                    mode='lines',
                    line=dict(width=2, color='#999999', dash='dot'),
                    hoverinfo='none',
                    showlegend=False
                )
            )
    
    node_x = []
    node_y = []
    node_text = []
    node_color = []
    node_size = []
    
    for node in G.nodes(data=True):
        x, y = pos[node[0]]
        node_x.append(x)
        node_y.append(y)
        
        if node[1].get('node_type') == 'coordinator':
            node_text.append('COORDINATOR')
            node_color.append('#00d4ff')
            node_size.append(60)
        else:
            state = env.get_city_state(node[0])
            node_text.append(f"{node[0].replace('_', ' ')}<br>Occ: {state['occupancy_rate']*100:.1f}%")
            
            if state['stress_level'] in ['CRITICAL', 'HIGH']:
                node_color.append('#ef4444')
            elif state['stress_level'] == 'MEDIUM':
                node_color.append('#f59e0b')
            else:
                node_color.append('#10b981')
            
            node_size.append(45)
    
    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        marker=dict(
            size=node_size,
            color=node_color,
            line=dict(width=3, color='white')
        ),
        text=node_text,
        textposition='top center',
        textfont=dict(size=11, color='#333333', family='Poppins', weight=600),
        hoverinfo='text'
    )
    
    fig = go.Figure(data=edge_trace_report + edge_trace_transfer + [node_trace])
    
    fig.update_layout(
        title=dict(text='Agent Communication Network', font=dict(size=20, color='#333333', weight=700)),
        showlegend=False,
        hovermode='closest',
        margin=dict(b=0, l=0, r=0, t=60),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=550,
        plot_bgcolor='#ffffff',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font=dict(family='Poppins, sans-serif')
    )
    
    return fig

def create_communication_flow_chart(messages_log):
    if not messages_log:
        return go.Figure()
    
    message_types = ['PERCEPTION', 'ALERT', 'OFFER', 'DECISION', 'REQUEST', 'TRANSFER']
    counts = {mt: 0 for mt in message_types}
    
    for msg in messages_log:
        if msg.type in counts:
            counts[msg.type] += 1
    
    fig = go.Figure(data=[
        go.Bar(
            x=list(counts.keys()),
            y=list(counts.values()),
            marker_color=['#3b82f6', '#ef4444', '#10b981', '#8b5cf6', '#f59e0b', '#00d4ff'],
            text=list(counts.values()),
            textposition='outside',
            textfont=dict(size=16, weight=700, color='#333333')
        )
    ])
    
    fig.update_layout(
        title=dict(text='Message Distribution by Type', font=dict(size=18, color='#333333', weight=700)),
        xaxis_title='Message Type',
        yaxis_title='Count',
        height=380,
        plot_bgcolor='#ffffff',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font=dict(family='Poppins, sans-serif', color='#333333')
    )
    
    return fig

def create_comparison_chart(before_data, after_data, cities):
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Before Coordination',
        x=cities,
        y=before_data,
        marker_color='#ef4444',
        text=[f'{val:.1f}%' for val in before_data],
        textposition='outside',
        textfont=dict(size=13, color='#333333', weight=700)
    ))
    
    fig.add_trace(go.Bar(
        name='After Coordination',
        x=cities,
        y=after_data,
        marker_color='#10b981',
        text=[f'{val:.1f}%' for val in after_data],
        textposition='outside',
        textfont=dict(size=13, color='#333333', weight=700)
    ))
    
    fig.add_hline(y=78, line_dash="dash", line_color="#ef4444", line_width=3,
                  annotation_text="Crisis Threshold", annotation_position="right",
                  annotation=dict(font=dict(color='#333333', size=12)))
    fig.add_hline(y=60, line_dash="dot", line_color="#f59e0b", line_width=2,
                  annotation_text="Warning Level", annotation_position="right",
                  annotation=dict(font=dict(color='#333333', size=12)))
    
    fig.update_layout(
        barmode='group',
        title=dict(text='Occupancy Rate: Before vs After Coordination', 
                  font=dict(size=20, weight=700, color='#333333')),
        xaxis_title='City',
        yaxis_title='Occupancy Rate (%)',
        height=480,
        plot_bgcolor='#ffffff',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1,
                   font=dict(color='#333333', size=12)),
        font=dict(family='Poppins, sans-serif', color='#333333')
    )
    
    return fig

def create_crisis_heatmap(env, bayesian):
    cities = env.cities
    metrics = ['Occupancy', 'Crisis Probability', 'Stress Level']
    
    data = []
    for city in cities:
        state = env.get_city_state(city)
        crisis_prob = bayesian.predict_crisis_probability(state)
        stress_map = {'LOW': 0.2, 'MEDIUM': 0.5, 'HIGH': 0.75, 'CRITICAL': 0.95}
        
        data.append([
            state['occupancy_rate'],
            crisis_prob,
            stress_map.get(state['stress_level'], 0.5)
        ])
    
    fig = go.Figure(data=go.Heatmap(
        z=np.array(data).T,
        x=[c.replace('_', ' ') for c in cities],
        y=metrics,
        colorscale='RdYlGn_r',
        text=[[f'{val:.2f}' for val in row] for row in np.array(data).T],
        texttemplate='%{text}',
        textfont={"size": 15, "weight": 700, "color": "#333333"},
        colorbar=dict(title="Risk Level")
    ))
    
    fig.update_layout(
        title=dict(text='Multi-Dimensional Risk Assessment Heatmap', 
                  font=dict(size=18, color='#333333', weight=700)),
        height=340,
        plot_bgcolor='#ffffff',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font=dict(family='Poppins, sans-serif', size=12, color='#333333')
    )
    
    return fig

def create_score_gauge(score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "System Performance", 'font': {'size': 22, 'weight': 700, 'color': '#333333'}},
        delta={'reference': 70, 'increasing': {'color': "#10b981"}},
        number={'font': {'size': 60, 'color': '#0066cc', 'weight': 800}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 2, 'tickcolor': "#333333"},
            'bar': {'color': "#00d4ff", 'thickness': 0.8},
            'bgcolor': "#ffffff",
            'borderwidth': 3,
            'bordercolor': "#00d4ff",
            'steps': [
                {'range': [0, 50], 'color': 'rgba(239, 68, 68, 0.2)'},
                {'range': [50, 75], 'color': 'rgba(245, 158, 11, 0.2)'},
                {'range': [75, 100], 'color': 'rgba(16, 185, 129, 0.2)'}
            ],
            'threshold': {
                'line': {'color': "#ef4444", 'width': 5},
                'thickness': 0.8,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        height=340,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font=dict(family='Poppins, sans-serif', color='#333333')
    )
    
    return fig

def create_agent_performance_chart(env, bayesian):
    agents_data = []
    
    for city in env.cities:
        state = env.get_city_state(city)
        crisis_prob = bayesian.predict_crisis_probability(state)
        ml_class = bayesian.classify_risk_ml(state)
        
        utility = 10 if state['occupancy_rate'] < 0.45 else \
                  7 if 0.45 <= state['occupancy_rate'] < 0.65 else \
                  5 if 0.65 <= state['occupancy_rate'] < 0.78 else 13
        
        agents_data.append({
            'Agent': city.replace('_', ' '),
            'Utility Score': utility,
            'Crisis Probability': crisis_prob * 100,
            'ML Classification': ml_class,
            'Status': state['stress_level']
        })
    
    df = pd.DataFrame(agents_data)
    
    fig = go.Figure()
    
    colors = {'HIGH_RISK': '#ef4444', 'MEDIUM_RISK': '#f59e0b', 'LOW_RISK': '#10b981'}
    
    for ml_class in df['ML Classification'].unique():
        df_class = df[df['ML Classification'] == ml_class]
        fig.add_trace(go.Bar(
            name=ml_class,
            x=df_class['Agent'],
            y=df_class['Utility Score'],
            marker_color=colors.get(ml_class, '#64748b'),
            text=df_class['Utility Score'],
            textposition='outside',
            textfont=dict(size=14, weight=700, color='#333333')
        ))
    
    fig.update_layout(
        title=dict(text='Agent Utility Scores by Risk Classification',
                  font=dict(size=18, color='#333333', weight=700)),
        xaxis_title='City Agent',
        yaxis_title='Utility Score',
        height=430,
        plot_bgcolor='#ffffff',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        barmode='group',
        font=dict(family='Poppins, sans-serif', color='#333333'),
        legend=dict(font=dict(color='#333333'))
    )
    
    return fig

def main():
    st.markdown("""
    <div class="header-container">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="flex: 1;">
                <h1 class="header-title">FIFA World Cup 2026</h1>
                <p class="header-subtitle">Multi-Agent Crisis Management System</p>
            </div>
            <div class="logo-container">
                <svg width="100" height="60" viewBox="0 0 100 60" xmlns="http://www.w3.org/2000/svg">
                    <text x="5" y="35" font-family="Arial Black" font-size="28" font-weight="bold" fill="white">ENP</text>
                </svg>
                <svg width="90" height="60" viewBox="0 0 100 60" xmlns="http://www.w3.org/2000/svg">
                    <text x="5" y="25" font-family="Arial Black" font-size="22" font-weight="bold" fill="white">FIFA</text>
                    <text x="5" y="45" font-family="Arial" font-size="14" fill="#b8d4e8">2026</text>
                </svg>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("## ⚙️ Configuration Panel")
    st.sidebar.markdown("### City Occupancy Parameters")
    
    cities_config = {}
    default_values = {
        'Los_Angeles': 0.60,
        'Mexico_City': 0.47,
        'New_York': 0.48,
        'Toronto': 0.84
    }
    
    for city, default in default_values.items():
        cities_config[city] = st.sidebar.slider(
            f"{city.replace('_', ' ')}",
            min_value=0.30,
            max_value=0.95,
            value=default,
            step=0.01,
            format="%.2f"
        )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### System Configuration")
    
    use_coordinator = st.sidebar.checkbox("Enable Coordinator Agent", value=True)
    show_messages = st.sidebar.checkbox("Show Communication Log", value=True)
    num_cycles = st.sidebar.selectbox("Simulation Cycles", [1, 2, 3], index=1)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Quick Scenarios")
    
    col1, col2, col3 = st.sidebar.columns(3)
    
    if col1.button("Normal"):
        for key in cities_config:
            cities_config[key] = np.random.uniform(0.45, 0.65)
        st.rerun()
    
    if col2.button("Warning"):
        cities_config['Los_Angeles'] = 0.72
        cities_config['Toronto'] = 0.68
        st.rerun()
    
    if col3.button("Crisis"):
        cities_config['Los_Angeles'] = 0.88
        cities_config['Toronto'] = 0.91
        cities_config['New_York'] = 0.42
        cities_config['Mexico_City'] = 0.39
        st.rerun()
    
    st.sidebar.markdown("---")
    run_button = st.sidebar.button("▶ RUN SIMULATION", type="primary")
    
    if run_button or 'initialized' not in st.session_state:
        st.session_state.initialized = True
        
        with st.spinner("Initializing multi-agent system..."):
            cities_data = {
                'Los_Angeles': {
                    'occupancy': cities_config['Los_Angeles'],
                    'capacity': 6659579,
                    'cluster': 1,
                    'popularity': 2,
                    'matches': 8
                },
                'Mexico_City': {
                    'occupancy': cities_config['Mexico_City'],
                    'capacity': 3736279,
                    'cluster': 0,
                    'popularity': 3,
                    'matches': 6
                },
                'New_York': {
                    'occupancy': cities_config['New_York'],
                    'capacity': 7240856,
                    'cluster': 1,
                    'popularity': 1,
                    'matches': 10
                },
                'Toronto': {
                    'occupancy': cities_config['Toronto'],
                    'capacity': 2598127,
                    'cluster': 0,
                    'popularity': 4,
                    'matches': 8
                }
            }
            
            env = EnvironmentHybrid(cities_data)
            bayesian = BayesianCrisisPredictor()
            coordinator = AgentCoordinator()
            
            before_occupancy = [env.dynamic_state[city]['occupancy_rate'] * 100 
                              for city in env.cities]
            score_initial = calculate_system_score(env)
            
            crises_detected = 0
            helpers_available = 0
            crises_list = []
            helpers_list = []
            
            if use_coordinator:
                crises_detected, helpers_available, crises_list, helpers_list = \
                    coordinator.detect_and_coordinate(env, bayesian)
            
            after_occupancy = [env.dynamic_state[city]['occupancy_rate'] * 100 
                             for city in env.cities]
            score_final = calculate_system_score(env)
            
            total_messages = len(env.messages_log)
            
            st.session_state.results = {
                'env': env,
                'coordinator': coordinator,
                'bayesian': bayesian,
                'score_initial': score_initial,
                'score_final': score_final,
                'crises_detected': crises_detected,
                'helpers_available': helpers_available,
                'use_coordinator': use_coordinator,
                'before_occupancy': before_occupancy,
                'after_occupancy': after_occupancy,
                'crises_list': crises_list,
                'helpers_list': helpers_list,
                'total_messages': total_messages
            }
    
    if 'results' in st.session_state:
        results = st.session_state.results
        env = results['env']
        coordinator = results['coordinator']
        bayesian = results['bayesian']
        
        st.markdown('<p class="section-header"> System Performance Dashboard</p>', unsafe_allow_html=True)
        
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        
        with col1:
            delta = results['score_final'] - results['score_initial']
            st.metric("System Score", 
                     f"{results['score_final']}/100",
                     f"{delta:+d} pts")
        
        with col2:
            st.metric("Crises Detected", results['crises_detected'])
        
        with col3:
            st.metric("Helper Cities", results['helpers_available'])
        
        with col4:
            if results['use_coordinator']:
                st.metric("Crises Resolved", coordinator.crises_resolved)
            else:
                st.metric("Coordinator", "OFF")
        
        with col5:
            st.metric("Transfers", len(coordinator.transfers_log))
        
        with col6:
            st.metric("Messages", results['total_messages'])
        
        st.markdown("---")
        
        if results['use_coordinator']:
            st.markdown('<p class="section-header"> Agent Communication Network</p>', unsafe_allow_html=True)
            
            col1, col2 = st.columns([3, 2])
            
            with col1:
                st.plotly_chart(create_agent_network_graph(coordinator, env), 
                              use_container_width=True)
                
                st.markdown("""
                <div style='background: #ffffff; 
                            padding: 1.5rem; border-radius: 12px; color: #333333; margin-top: 1rem;
                            border: 2px solid #e0e0e0; box-shadow: 0 4px 15px rgba(0,0,0,0.08);'>
                <strong style='color: #0066cc; font-size: 1.1rem;'>Network Legend:</strong><br><br>
                <span style='color: #00d4ff;'>● Cyan Node:</span> Coordinator (central orchestrator)<br>
                <span style='color: #10b981;'>● Green Nodes:</span> Stable agents (can offer help)<br>
                <span style='color: #f59e0b;'>● Orange Nodes:</span> Warning level agents<br>
                <span style='color: #ef4444;'>● Red Nodes:</span> Crisis agents (need assistance)<br>
                <span style='color: #999999;'>⋯ Dotted Lines:</span> Status reports to coordinator<br>
                <span style='color: #00d4ff;'>─ Solid Cyan Lines:</span> Resource transfers
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.plotly_chart(create_communication_flow_chart(env.messages_log),
                              use_container_width=True)
                
                st.markdown(f"""
                <div class="communication-stats">
                    <h3 style="margin: 0;">Communication Statistics</h3>
                    <p style="font-size: 3rem; margin: 1rem 0; font-weight: 800;">{results['total_messages']}</p>
                    <p style="font-size: 1rem; margin: 0;">Total Messages Exchanged</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("##### Agent Activity")
                for city in env.cities:
                    state = env.get_city_state(city)
                    st.markdown(f"""
                    <div class="agent-status-card">
                        <strong style='font-size: 1.05rem;'>{city.replace('_', ' ')}</strong>
                        <span class="badge-{'active' if state['messages_sent'] > 0 else 'inactive'}">
                            {'ACTIVE' if state['messages_sent'] > 0 else 'IDLE'}
                        </span>
                        <br>
                        <small style='color: #666666;'>Sent: {state['messages_sent']} | Received: {state['messages_received']}</small>
                    </div>
                    """, unsafe_allow_html=True)
        
        if show_messages and env.messages_log:
            st.markdown('<p class="section-header"> Real-Time Communication Log</p>', unsafe_allow_html=True)
            
            log_html = '<div class="message-log">'
            for msg in env.messages_log[-20:]:
                msg_class = f"message-{msg.type.lower()}"
                timestamp = msg.timestamp.strftime("%H:%M:%S")
                log_html += f'<div class="message-line {msg_class}">'
                log_html += f'<strong>[{timestamp}]</strong> <span style="color: #0066cc;">{msg.type}</span> | '
                log_html += f'<strong>{msg.sender}</strong> → <strong>{msg.receiver}</strong>: {msg.content}'
                log_html += '</div>'
            log_html += '</div>'
            
            st.markdown(log_html, unsafe_allow_html=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.plotly_chart(
                create_comparison_chart(
                    results['before_occupancy'],
                    results['after_occupancy'],
                    [c.replace('_', ' ') for c in env.cities]
                ),
                use_container_width=True
            )
        
        with col2:
            st.plotly_chart(create_score_gauge(results['score_final']), 
                          use_container_width=True)
        
        st.markdown('<p class="section-header"> AI Analysis & Predictions</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(create_crisis_heatmap(env, bayesian), 
                          use_container_width=True)
        
        with col2:
            st.plotly_chart(create_agent_performance_chart(env, bayesian),
                          use_container_width=True)
        
        st.markdown('<p class="section-header"> Detailed City Analysis</p>', unsafe_allow_html=True)
        
        for city in env.cities:
            state = env.get_city_state(city)
            crisis_prob = bayesian.predict_crisis_probability(state)
            ml_class = bayesian.classify_risk_ml(state)
            recommendation = bayesian.get_recommendations(state)
            
            with st.expander(f" {city.replace('_', ' ')} - {state['stress_level']} STATUS", expanded=False):
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Occupancy Rate", f"{state['occupancy_rate']*100:.1f}%")
                
                with col2:
                    st.metric("Crisis Probability", f"{crisis_prob*100:.1f}%")
                
                with col3:
                    st.metric("Available Rooms", f"{state['available_rooms']:,}")
                
                with col4:
                    st.metric("ML Classification", ml_class)
                
                st.markdown(f"<p style='color: #0066cc; font-weight: 600;'>AI Recommendation: {recommendation}</p>", unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"<p style='color: #333333;'><strong>Messages Sent:</strong> {state['messages_sent']}</p>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"<p style='color: #333333;'><strong>Messages Received:</strong> {state['messages_received']}</p>", unsafe_allow_html=True)
                
                if state['resources_received'] > 0:
                    st.success(f"✓ Received {state['resources_received']:,} rooms from helper cities")
                if state['resources_given'] > 0:
                    st.info(f"→ Provided {state['resources_given']:,} rooms to crisis cities")
        
        if results['use_coordinator'] and coordinator.transfers_log:
            st.markdown('<p class="section-header">Coordination Timeline</p>', unsafe_allow_html=True)
            
            for i, transfer in enumerate(coordinator.transfers_log, 1):
                st.markdown(f"""
                <div class="timeline-item">
                    <strong style='color: #0066cc; font-size: 1.1rem;'>Transfer #{i}</strong><br><br>
                    <span style='color: #333333;'>From: <strong style='color: #10b981;'>{transfer['from'].replace('_', ' ')}</strong> → 
                    To: <strong style='color: #ef4444;'>{transfer['to'].replace('_', ' ')}</strong></span><br>
                    <span style='color: #666666;'>Reduction: <strong>{transfer['reduction']*100:.0f}%</strong> | 
                    Crisis Probability: <strong>{transfer['crisis_prob']*100:.1f}%</strong></span>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header"> Detailed Statistics</p>', unsafe_allow_html=True)
        
        stats_data = []
        for city in env.cities:
            state = env.get_city_state(city)
            crisis_prob = bayesian.predict_crisis_probability(state)
            
            stats_data.append({
                'City': city.replace('_', ' '),
                'Occupancy': f"{state['occupancy_rate']*100:.1f}%",
                'Available Rooms': f"{state['available_rooms']:,}",
                'Total Capacity': f"{state['capacity']:,}",
                'Crisis Probability': f"{crisis_prob*100:.1f}%",
                'Matches Hosted': state['num_matches'],
                'Cluster': f"Cluster {state['cluster']}",
                'Status': state['stress_level'],
                'Messages Sent': state['messages_sent'],
                'Messages Received': state['messages_received']
            })
        
        df_stats = pd.DataFrame(stats_data)
        st.dataframe(df_stats, use_container_width=True, hide_index=True)
        
        export_col1, export_col2 = st.columns([3, 1])
        with export_col2:
            csv = df_stats.to_csv(index=False)
            st.download_button(
                label=" Export Report (CSV)",
                data=csv,
                file_name=f"fifa2026_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
    
    st.markdown("""
    <div class="footer-container">
        <p class="footer-title">FIFA WORLD CUP 2026 - MULTI-AGENT CRISIS MANAGEMENT SYSTEM</p>
        <p class="footer-authors">Developed by <strong>SADOUN Kahina Melissa</strong> & <strong>BENDAIKHA Meriem</strong></p>
        <p class="footer-subtitle">BIG DATA × IIA Project</p>
        <p class="footer-subtitle">Coordinated by <strong>Madam BELDJOUDI Samia</strong></p>
        <p class="footer-subtitle" style="margin-top: 1rem; font-size: 0.85rem;">École Nationale Polytechnique - 2026</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

