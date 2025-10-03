# dashboard_livres_sacres.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuration de la page
st.set_page_config(
    page_title="Dashboard Comparatif - Livres Sacrés",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(45deg, #2E86AB, #A23B72);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    .book-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .quran-card { border-left-color: #2E86AB; }
    .torah-card { border-left-color: #A23B72; }
    .bible-card { border-left-color: #F18F01; }
    .section-header {
        color: #2E86AB;
        border-bottom: 3px solid #2E86AB;
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
        font-weight: bold;
    }
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

class SacredBooksDashboard:
    def __init__(self):
        self.books_data = self.load_books_data()
        self.comparison_data = self.load_comparison_data()
        
    def load_books_data(self):
        """Charge les données détaillées pour chaque livre"""
        books = {
            'Coran': {
                'nom_complet': 'Al-Quran (القرآن)',
                'religion': 'Islam',
                'langue_originale': 'Arabe',
                'date_revelation': '610-632 EC',
                'nombre_sourates': 114,
                'nombre_versets': 6236,
                'nombre_mots': 77439,
                'nombre_lettres': 323015,
                'periodicite_revelation': '23 ans',
                'lieu_revelation': 'La Mecque et Médine',
                'conservation': 'Mémorisation et écriture',
                'style': 'Poétique et rythmé',
                'theme_principal': 'Monothéisme, Législation, Éthique',
                'division_principale': 'Sourates, Versets',
                'premier_verset': "Lis au nom de ton Seigneur qui a créé",
                'dernier_verset': "Et craignez le jour où vous serez ramenés vers Allah",
                'couleur': '#2E86AB'
            },
            'Torah': {
                'nom_complet': 'Torah (תּוֹרָה)',
                'religion': 'Judaïsme',
                'langue_originale': 'Hébreu',
                'date_revelation': 'XIIIe siècle AEC (tradition)',
                'nombre_sourates': 5,
                'nombre_versets': 5845,
                'nombre_mots': 79258,
                'nombre_lettres': 304805,
                'periodicite_revelation': '40 jours (Mont Sinaï)',
                'lieu_revelation': 'Mont Sinaï',
                'conservation': 'Rouleaux manuscrits',
                'style': 'Narratif et législatif',
                'theme_principal': 'Alliance, Loi, Histoire des Patriarches',
                'division_principale': 'Livres, Parashiyot',
                'premier_verset': "Au commencement, Dieu créa les cieux et la terre",
                'dernier_verset': "Et il n'a plus paru en Israël de prophète comme Moïse",
                'couleur': '#A23B72'
            },
            'Bible': {
                'nom_complet': 'Bible (Βίβλος)',
                'religion': 'Christianisme',
                'langue_originale': 'Hébreu, Araméen, Grec',
                'date_revelation': '1500 AEC - 100 EC',
                'nombre_sourates': 73,
                'nombre_versets': 35678,
                'nombre_mots': 727969,
                'nombre_lettres': 3100000,
                'periodicite_revelation': '1600 ans',
                'lieu_revelation': 'Moyen-Orient, Méditerranée',
                'conservation': 'Manuscrits, Codex',
                'style': 'Narratif, Poétique, Épistolaire',
                'theme_principal': 'Salut, Amour, Rédemption',
                'division_principale': 'Ancien/Nouveau Testament, Livres',
                'premier_verset': "Au commencement, Dieu créa les cieux et la terre",
                'dernier_verset': "Que la grâce du Seigneur Jésus soit avec tous",
                'couleur': '#F18F01'
            }
        }
        return books
    
    def load_comparison_data(self):
        """Charge les données pour la comparaison"""
        # Données pour les graphiques comparatifs
        data = {
            'Livre': ['Coran', 'Torah', 'Bible'],
            'Nombre de versets': [6236, 5845, 35678],
            'Nombre de mots': [77439, 79258, 727969],
            'Durée révélation (années)': [23, 1, 1600],
            'Nombre de langues traduit': [150, 10, 3500],
            'Nombre de religions': [1, 1, 3],
            'Années depuis révélation': [1400, 3300, 2000],
            'Pourcentage monde influencé': [24, 0.2, 33]
        }
        return pd.DataFrame(data)
    
    def display_header(self):
        """Affiche l'en-tête du dashboard"""
        st.markdown('<h1 class="main-header">📚 Dashboard Comparatif - Livres Sacrés</h1>', 
                   unsafe_allow_html=True)
        
        st.markdown("""
        <div style='text-align: center; color: #666; margin-bottom: 2rem;'>
        Analyse comparative du Coran, de la Torah et de la Bible : structure, histoire et influence
        </div>
        """, unsafe_allow_html=True)
        
        # Métriques principales
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_versets = self.comparison_data['Nombre de versets'].sum()
            st.metric("Total des versets", f"{total_versets:,}")
        
        with col2:
            total_mots = self.comparison_data['Nombre de mots'].sum()
            st.metric("Total des mots", f"{total_mots:,}")
        
        with col3:
            annees_revelation = self.comparison_data['Durée révélation (années)'].sum()
            st.metric("Années de révélation", annees_revelation)
        
        with col4:
            traductions = self.comparison_data['Nombre de langues traduit'].sum()
            st.metric("Langues de traduction", f"{traductions:,}")

    def create_book_cards(self):
        """Affiche les cartes détaillées pour chaque livre"""
        st.markdown('<h3 class="section-header">📖 Présentation des Livres Sacrés</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        for idx, (book_name, book_data) in enumerate(self.books_data.items()):
            with [col1, col2, col3][idx]:
                st.markdown(f"""
                <div class='book-card {book_name.lower()}-card'>
                    <h3 style='color: {book_data["couleur"]}; margin-top: 0;'>{book_name}</h3>
                    <p><strong>Nom complet:</strong> {book_data['nom_complet']}</p>
                    <p><strong>Religion:</strong> {book_data['religion']}</p>
                    <p><strong>Langue originale:</strong> {book_data['langue_originale']}</p>
                    <p><strong>Période de révélation:</strong> {book_data['date_revelation']}</p>
                    <p><strong>Style:</strong> {book_data['style']}</p>
                    <p><strong>Thème principal:</strong> {book_data['theme_principal']}</p>
                </div>
                """, unsafe_allow_html=True)

    def create_structure_comparison(self):
        """Crée la comparaison structurelle"""
        st.markdown('<h3 class="section-header">📊 Analyse Structurelle</h3>', 
                   unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["📐 Dimensions", "📈 Visualisations", "🔍 Détails"])
        
        with tab1:
            col1, col2 = st.columns(2)
            
            with col1:
                # Graphique barres - nombre de versets
                fig = px.bar(self.comparison_data, x='Livre', y='Nombre de versets',
                            color='Livre', color_discrete_map={
                                'Coran': '#2E86AB',
                                'Torah': '#A23B72', 
                                'Bible': '#F18F01'
                            },
                            title="Nombre de Versets par Livre")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Graphique barres - nombre de mots
                fig = px.bar(self.comparison_data, x='Livre', y='Nombre de mots',
                            color='Livre', color_discrete_map={
                                'Coran': '#2E86AB',
                                'Torah': '#A23B72',
                                'Bible': '#F18F01'
                            },
                            title="Nombre de Mots par Livre")
                st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            col1, col2 = st.columns(2)
            
            with col1:
                # Radar chart pour comparaison multi-dimensionnelle
                dimensions = ['Nombre de versets', 'Nombre de mots', 'Durée révélation (années)', 
                             'Nombre de langues traduit', 'Pourcentage monde influencé']
                
                fig = go.Figure()
                
                for book in self.comparison_data['Livre'].unique():
                    book_data = self.comparison_data[self.comparison_data['Livre'] == book]
                    values = [book_data[dim].values[0] for dim in dimensions]
                    
                    # Normalisation pour le radar chart
                    max_vals = [max(self.comparison_data[dim]) for dim in dimensions]
                    normalized_values = [v/max_v * 100 for v, max_v in zip(values, max_vals)]
                    
                    fig.add_trace(go.Scatterpolar(
                        r=normalized_values,
                        theta=dimensions,
                        fill='toself',
                        name=book,
                        line=dict(color=self.books_data[book]['couleur'])
                    ))
                
                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(visible=True, range=[0, 100])
                    ),
                    showlegend=True,
                    title="Profil Comparatif des Livres Sacrés",
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Diagrame en bulles
                fig = px.scatter(self.comparison_data, 
                               x='Nombre de versets', 
                               y='Nombre de mots',
                               size='Durée révélation (années)',
                               color='Livre',
                               hover_name='Livre',
                               size_max=60,
                               color_discrete_map={
                                   'Coran': '#2E86AB',
                                   'Torah': '#A23B72',
                                   'Bible': '#F18F01'
                               },
                               title="Relation Versets-Mots-Durée")
                st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            # Tableau détaillé de comparaison
            st.subheader("Tableau Comparatif Détaillé")
            
            comparison_details = []
            for book_name, book_data in self.books_data.items():
                comparison_details.append({
                    'Livre': book_name,
                    'Religion': book_data['religion'],
                    'Langue originale': book_data['langue_originale'],
                    'Période révélation': book_data['date_revelation'],
                    'Durée révélation': book_data['periodicite_revelation'],
                    'Nombre divisions': book_data['nombre_sourates'],
                    'Lieu révélation': book_data['lieu_revelation'],
                    'Méthode conservation': book_data['conservation']
                })
            
            details_df = pd.DataFrame(comparison_details)
            st.dataframe(details_df, use_container_width=True)

    def create_historical_timeline(self):
        """Crée la frise chronologique historique"""
        st.markdown('<h3 class="section-header">🕰️ Frise Chronologique</h3>', 
                   unsafe_allow_html=True)
        
        # Données pour la frise chronologique
        timeline_data = [
            {'Événement': 'Révélation Torah', 'Année': -1300, 'Livre': 'Torah', 'Description': 'Révélation à Moïse au Mont Sinaï'},
            {'Événement': 'Rédaction Bible AT', 'Année': -1000, 'Livre': 'Bible', 'Description': 'Début rédaction Ancien Testament'},
            {'Événement': 'Compilation Torah', 'Année': -500, 'Livre': 'Torah', 'Description': 'Compilation finale de la Torah'},
            {'Événement': 'Révélation Coran', 'Année': 610, 'Livre': 'Coran', 'Description': 'Début révélation à Mahomet'},
            {'Événement': 'Compilation Coran', 'Année': 650, 'Livre': 'Coran', 'Description': 'Compilation sous Calife Othman'},
            {'Événement': 'Rédaction Bible NT', 'Année': 50, 'Livre': 'Bible', 'Description': 'Rédaction Nouveau Testament'},
            {'Événement': 'Canon Bible', 'Année': 400, 'Livre': 'Bible', 'Description': 'Établissement du canon biblique'},
            {'Événement': 'Traduction Bible', 'Année': 1382, 'Livre': 'Bible', 'Description': 'Première traduction complète'},
            {'Événement': 'Impression Bible', 'Année': 1455, 'Livre': 'Bible', 'Description': 'Bible de Gutenberg'},
        ]
        
        timeline_df = pd.DataFrame(timeline_data)
        
        # Création de la frise chronologique
        fig = px.scatter(timeline_df, x='Année', y='Livre', color='Livre',
                        size=[10]*len(timeline_df),  # Taille constante des points
                        hover_data=['Description'],
                        color_discrete_map={
                            'Coran': '#2E86AB',
                            'Torah': '#A23B72',
                            'Bible': '#F18F01'
                        },
                        title="Frise Chronologique des Livres Sacrés")
        
        # Ajout des lignes de connexion
        for _, row in timeline_df.iterrows():
            fig.add_annotation(
                x=row['Année'],
                y=row['Livre'],
                text=row['Événement'],
                showarrow=True,
                arrowhead=1,
                ax=0,
                ay=-40
            )
        
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    def create_influence_analysis(self):
        """Analyse de l'influence mondiale"""
        st.markdown('<h3 class="section-header">🌍 Influence et Diffusion</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Carte de diffusion mondiale
            diffusion_data = {
                'Pays': ['Monde Arabe', 'Europe', 'Amériques', 'Afrique', 'Asie'],
                'Coran': [90, 5, 3, 40, 20],
                'Torah': [0.1, 0.5, 2, 0.1, 0.1],
                'Bible': [10, 70, 85, 60, 15]
            }
            diffusion_df = pd.DataFrame(diffusion_data)
            
            fig = go.Figure()
            
            fig.add_trace(go.Bar(name='Coran', x=diffusion_df['Pays'], y=diffusion_df['Coran'],
                                marker_color='#2E86AB'))
            fig.add_trace(go.Bar(name='Torah', x=diffusion_df['Pays'], y=diffusion_df['Torah'],
                                marker_color='#A23B72'))
            fig.add_trace(go.Bar(name='Bible', x=diffusion_df['Pays'], y=diffusion_df['Bible'],
                                marker_color='#F18F01'))
            
            fig.update_layout(
                title="Diffusion Géographique (%)",
                barmode='group',
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Impact culturel
            impact_data = {
                'Domaine': ['Art', 'Musique', 'Littérature', 'Droit', 'Éducation'],
                'Coran': [8, 7, 9, 9, 8],
                'Torah': [7, 6, 8, 8, 7],
                'Bible': [9, 9, 9, 8, 8]
            }
            impact_df = pd.DataFrame(impact_data)
            
            fig = px.line(impact_df, x='Domaine', y=['Coran', 'Torah', 'Bible'],
                         title="Impact Culturel par Domaine (1-10)",
                         color_discrete_map={
                             'Coran': '#2E86AB',
                             'Torah': '#A23B72',
                             'Bible': '#F18F01'
                         })
            
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

    def create_thematic_analysis(self):
        """Analyse thématique comparative"""
        st.markdown('<h3 class="section-header">🎭 Analyse Thématique</h3>', 
                   unsafe_allow_html=True)
        
        # Données des thèmes principaux
        themes_data = {
            'Thème': ['Monothéisme', 'Prophètes', 'Loi Divine', 'Éthique', 'Histoire Sacrée', 'Salut', 'Fin des Temps'],
            'Coran': [95, 90, 85, 80, 70, 75, 65],
            'Torah': [90, 80, 95, 75, 90, 60, 50],
            'Bible': [85, 85, 70, 85, 80, 95, 80]
        }
        themes_df = pd.DataFrame(themes_data)
        
        # Heatmap des thèmes
        fig = px.imshow(themes_df.set_index('Thème'),
                       title="Importance Relative des Thèmes (%)",
                       color_continuous_scale='Viridis',
                       aspect="auto")
        
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
        
        # Analyse détaillée par livre
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("🎯 Coran - Thèmes Clés")
            st.markdown("""
            - **Tawhid** (Unicité divine)
            - **Prophétologie**
            - **Législation sociale**
            - **Éthique individuelle**
            - **Comptes finals**
            """)
        
        with col2:
            st.subheader("📜 Torah - Thèmes Clés")
            st.markdown("""
            - **Alliance divine**
            - **Loi mosaïque**
            - **Histoire patriarcale**
            - **Pureté rituelle**
            - **Terre promise**
            """)
        
        with col3:
            st.subheader("✝️ Bible - Thèmes Clés")
            st.markdown("""
            - **Salvation**
            - **Amour divin**
            - **Rédemption**
            - **Grâce**
            - **Royaume de Dieu**
            """)

    def create_sidebar(self):
        """Crée la sidebar avec les contrôles"""
        st.sidebar.markdown("## 🎛️ Contrôles d'Analyse")
        
        # Sélecteur de focus
        analysis_focus = st.sidebar.selectbox(
            "Focus d'analyse",
            ["Vue d'ensemble", "Structure", "Histoire", "Influence", "Thématiques"]
        )
        
        # Filtre des livres
        st.sidebar.markdown("### 📚 Livres à Afficher")
        show_quran = st.sidebar.checkbox("Coran", True)
        show_torah = st.sidebar.checkbox("Torah", True)
        show_bible = st.sidebar.checkbox("Bible", True)
        
        # Métriques rapides
        st.sidebar.markdown("### 📊 Statistiques Globales")
        total_books = sum([show_quran, show_torah, show_bible])
        total_verses = sum([self.books_data[book]['nombre_versets'] for book in ['Coran', 'Torah', 'Bible'] 
                          if (book == 'Coran' and show_quran) or (book == 'Torah' and show_torah) or (book == 'Bible' and show_bible)])
        
        st.sidebar.metric("Livres affichés", total_books)
        st.sidebar.metric("Versets totaux", f"{total_verses:,}")
        
        return {
            'analysis_focus': analysis_focus,
            'show_quran': show_quran,
            'show_torah': show_torah,
            'show_bible': show_bible
        }

    def run_dashboard(self):
        """Exécute le dashboard complet"""
        # Sidebar
        controls = self.create_sidebar()
        
        # Header
        self.display_header()
        
        # Cartes des livres
        self.create_book_cards()
        
        # Navigation par onglets
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Structure", 
            "🕰️ Histoire", 
            "🌍 Influence", 
            "🎭 Thématiques"
        ])
        
        with tab1:
            self.create_structure_comparison()
        
        with tab2:
            self.create_historical_timeline()
        
        with tab3:
            self.create_influence_analysis()
        
        with tab4:
            self.create_thematic_analysis()
        
        # Footer
        st.markdown("---")
        st.markdown("""
        **Sources:** Données religieuses et historiques consolidées  
        **Framework:** Streamlit • Plotly • Pandas  
        **Objectif:** Analyse comparative objective des textes sacrés  
        *Données à but éducatif et informatif*
        """)

# Lancement du dashboard
if __name__ == "__main__":
    dashboard = SacredBooksDashboard()
    dashboard.run_dashboard()