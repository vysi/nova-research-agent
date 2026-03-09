import streamlit as st
from nova_client import NovaClient
from research_engine import ResearchEngine
from utils import (
    calculate_source_relevance,
    extract_key_terms,
    calculate_synthesis_quality,
    calculate_diversity_score,
    format_timestamp,
    generate_research_summary_stats,
    truncate_text
)
from demo_mode import is_demo_mode, get_demo_synthesis, get_demo_sources, get_demo_insights
import json
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from collections import Counter
import re

# Page configuration
st.set_page_config(
    page_title="Nova Research Agent - AI-Powered Research Assistant",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Check if demo mode
DEMO_MODE = is_demo_mode()

# Initialize session state
if 'research_history' not in st.session_state:
    st.session_state.research_history = []
if 'current_research' not in st.session_state:
    st.session_state.current_research = None
if 'nova_client' not in st.session_state:
    if not DEMO_MODE:
        st.session_state.nova_client = NovaClient()
    else:
        st.session_state.nova_client = None
if 'research_engine' not in st.session_state:
    st.session_state.research_engine = ResearchEngine()

# Header with impressive styling
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("🔬 Nova Research Agent")
    st.markdown("### *Powered by Amazon Nova AI*")
    if DEMO_MODE:
        st.warning("⚠️ DEMO MODE - Configure AWS credentials in .env to use real Nova AI")
    else:
        st.caption("Transform hours of research into seconds of intelligence")

# Add metrics banner
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
with metric_col1:
    st.metric("Research Queries", len(st.session_state.research_history))
with metric_col2:
    total_sources = sum(len(r.get('sources', [])) for r in st.session_state.research_history)
    st.metric("Sources Analyzed", total_sources)
with metric_col3:
    if DEMO_MODE:
        st.metric("AI Model", "Demo Mode")
    else:
        st.metric("AI Model", "Nova Pro")
with metric_col4:
    st.metric("Status", "🟢 Active")

# Sidebar
with st.sidebar:
    st.image("https://img.shields.io/badge/Amazon%20Nova-AI%20Powered-FF9900?style=for-the-badge&logo=amazon-aws", use_container_width=True)
    
    st.header("✨ Features")
    st.markdown("""
    - 🔍 **Multi-Source Search** - Gather from web
    - 🤖 **AI Synthesis** - Nova-powered analysis
    - 📊 **Smart Insights** - Key findings extraction
    - 💬 **Interactive Q&A** - Ask anything
    - 📥 **Export Ready** - Multiple formats
    - 🎯 **Citation Tracking** - Full transparency
    """)
    
    st.divider()
    
    st.header("⚙️ Settings")
    max_sources = st.slider("Max sources", 3, 10, 5, help="Number of sources to analyze")
    temperature = st.slider("AI Creativity", 0.0, 1.0, 0.5, 0.1, help="Higher = more creative")
    
    show_advanced = st.checkbox("Show advanced options", False)
    if show_advanced:
        model_choice = st.selectbox("Nova Model", ["Nova Pro (Recommended)", "Nova Lite (Faster)"])
        include_snippets = st.checkbox("Include source snippets", True)
    
    st.divider()
    
    if st.session_state.research_history:
        st.header("📚 Recent Research")
        for i, research in enumerate(reversed(st.session_state.research_history[-5:])):
            with st.expander(f"🔖 {research['query'][:40]}..."):
                st.caption(f"⏰ {research['timestamp'][:19]}")
                st.caption(f"📄 {len(research['sources'])} sources")
                if st.button("Load", key=f"load_history_{i}"):
                    st.session_state.current_research = research
                    st.rerun()
    
    st.divider()
    st.caption("🏆 Built for Amazon Nova AI Hackathon 2026")
    st.caption("Made with ❤️ using Amazon Nova")

# Main content
tab1, tab2, tab3, tab4 = st.tabs(["🔍 New Research", "📊 Results & Insights", "💬 Q&A", "📈 Analytics"])

with tab1:
    st.header("Start Your Research Journey")
    
    # Quick examples
    with st.expander("💡 Example Research Questions"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Technology:**
            - Latest quantum computing breakthroughs
            - AI trends in healthcare 2026
            - Sustainable energy innovations
            """)
        with col2:
            st.markdown("""
            **Business:**
            - Electric vehicle market analysis
            - Remote work productivity studies
            - Cryptocurrency regulation updates
            """)
    
    research_query = st.text_area(
        "What would you like to research?",
        placeholder="e.g., What are the latest developments in quantum computing and their practical applications?",
        height=120,
        help="Enter any research question - the more specific, the better!"
    )
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        research_button = st.button("🚀 Start Research", type="primary", use_container_width=True)
    with col2:
        if st.button("🎲 Random Topic", use_container_width=True):
            topics = [
                "What are the latest breakthroughs in fusion energy?",
                "How is AI transforming drug discovery in 2026?",
                "What are the emerging trends in space exploration?",
                "How are quantum computers being used commercially?",
                "What are the latest developments in brain-computer interfaces?"
            ]
            import random
            st.session_state.random_query = random.choice(topics)
            st.rerun()
    
    if hasattr(st.session_state, 'random_query'):
        research_query = st.session_state.random_query
        del st.session_state.random_query
    
    if research_button and research_query:
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        with st.spinner("🔍 Searching sources..."):
            status_text.text("🌐 Searching the web...")
            progress_bar.progress(20)
            
            # Gather sources
            sources = st.session_state.research_engine.gather_research(research_query)
            
            if not sources:
                st.error("❌ No sources found. Please try a different query.")
                progress_bar.empty()
                status_text.empty()
            else:
                progress_bar.progress(50)
                status_text.text(f"✅ Found {len(sources)} sources!")
                
                # Show sources in a nice format
                with st.expander(f"📚 {len(sources)} Sources Discovered", expanded=True):
                    for i, source in enumerate(sources):
                        col1, col2 = st.columns([4, 1])
                        with col1:
                            st.markdown(f"**{i+1}. [{source['title']}]({source['url']})**")
                            st.caption(source['snippet'][:150] + "...")
                        with col2:
                            st.caption(f"✅ Verified")
        
        if sources:
            status_text.text("🤖 Analyzing with Amazon Nova AI...")
            progress_bar.progress(70)
            
            with st.spinner("🧠 AI is synthesizing information..."):
                # Synthesize research
                if DEMO_MODE:
                    # Use demo mode
                    synthesis = get_demo_synthesis(research_query)
                    key_insights = get_demo_insights()
                else:
                    # Use real Nova AI
                    synthesis = st.session_state.nova_client.synthesize_research(
                        sources=sources,
                        query=research_query
                    )
                    
                    progress_bar.progress(90)
                    status_text.text("✨ Generating insights...")
                    
                    # Extract key insights
                    key_insights = st.session_state.nova_client.extract_insights(synthesis)
                
                progress_bar.progress(100)
                status_text.text("✅ Research complete!")
                
                # Save research
                research_data = {
                    'query': research_query,
                    'sources': sources,
                    'synthesis': synthesis,
                    'insights': key_insights,
                    'timestamp': datetime.now().isoformat()
                }
                
                st.session_state.current_research = research_data
                st.session_state.research_history.append(research_data)
                
                st.success("🎉 Research complete! Check the Results tab.")
                st.balloons()
                
                # Auto-switch to results tab
                st.info("👉 Navigate to the 'Results & Insights' tab to view your research!")

with tab2:
    if st.session_state.current_research:
        research = st.session_state.current_research
        
        # Header with metadata
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.header(f"📊 {research['query']}")
        with col2:
            st.metric("Sources", len(research['sources']))
        with col3:
            st.caption(f"⏰ {research['timestamp'][:19]}")
        
        st.divider()
        
        # Key Insights Section (NEW!)
        if 'insights' in research:
            st.subheader("💡 Key Insights")
            insights_container = st.container()
            with insights_container:
                cols = st.columns(3)
                insights_list = research['insights'].split('\n') if isinstance(research['insights'], str) else research['insights']
                for i, insight in enumerate(insights_list[:6]):
                    if insight.strip():
                        with cols[i % 3]:
                            st.info(f"✨ {insight.strip()}")
            st.divider()
        
        # Main Synthesis
        st.subheader("📝 Comprehensive Research Summary")
        
        # Add a nice container for the synthesis
        with st.container():
            st.markdown(research['synthesis'])
        
        st.divider()
        
        # Source Analysis Visualization (NEW!)
        st.subheader("📈 Source Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Source credibility chart with REAL scores
            source_relevance = []
            for source in research['sources']:
                score = calculate_source_relevance(source, research['query'])
                source_relevance.append(score)
            
            source_data = {
                'Source': [f"Source {i+1}" for i in range(len(research['sources']))],
                'Relevance': source_relevance
            }
            fig = px.bar(source_data, x='Source', y='Relevance', 
                        title='Source Relevance Score (Algorithm-Based)',
                        color='Relevance',
                        color_continuous_scale='Viridis',
                        range_y=[0, 100])
            fig.update_layout(showlegend=False, height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Word frequency in synthesis - REAL analysis
            key_terms = extract_key_terms(research['synthesis'], top_n=10)
            
            if key_terms:
                fig = go.Figure(data=[go.Pie(labels=list(key_terms.keys()), 
                                             values=list(key_terms.values()),
                                             hole=.3)])
                fig.update_layout(title='Key Terms Distribution (Real Analysis)', height=300)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No key terms extracted yet")
        
        st.divider()
        
        # Sources Detail
        st.subheader("📚 Detailed Sources")
        for i, source in enumerate(research['sources']):
            with st.expander(f"📄 Source {i+1}: {source['title']}", expanded=False):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**URL:** [{source['url']}]({source['url']})")
                    st.markdown(f"**Snippet:** {source['snippet']}")
                with col2:
                    if st.button(f"📋 Summarize", key=f"summarize_{i}"):
                        with st.spinner("Summarizing..."):
                            summary = st.session_state.nova_client.summarize_content(
                                source['content']
                            )
                            st.markdown("**AI Summary:**")
                            st.success(summary)
        
        st.divider()
        
        # Export Section
        st.subheader("📥 Export Your Research")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            json_data = json.dumps(research, indent=2)
            st.download_button(
                "📄 JSON",
                data=json_data,
                file_name=f"research_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
        
        with col2:
            text_export = f"""RESEARCH REPORT
{'='*50}

Query: {research['query']}
Date: {research['timestamp']}

SUMMARY:
{research['synthesis']}

SOURCES:
"""
            for i, source in enumerate(research['sources']):
                text_export += f"\n{i+1}. {source['title']}\n   {source['url']}\n"
            
            st.download_button(
                "📝 Text",
                data=text_export,
                file_name=f"research_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        with col3:
            # Markdown export
            md_export = f"""# {research['query']}

*Generated: {research['timestamp']}*

## Summary

{research['synthesis']}

## Sources

"""
            for i, source in enumerate(research['sources']):
                md_export += f"{i+1}. [{source['title']}]({source['url']})\n"
            
            st.download_button(
                "📋 Markdown",
                data=md_export,
                file_name=f"research_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                mime="text/markdown",
                use_container_width=True
            )
        
        with col4:
            if st.button("🔄 New Research", use_container_width=True):
                st.session_state.current_research = None
                st.rerun()
    
    else:
        st.info("👈 Start a new research query to see results here!")
        st.image("https://via.placeholder.com/800x400/667eea/ffffff?text=Start+Your+Research+Journey", use_container_width=True)

with tab3:
    if st.session_state.current_research:
        st.header("💬 Interactive Q&A")
        st.markdown("Ask follow-up questions about your research. Nova AI will answer based on the sources.")
        
        # Chat history
        if 'qa_history' not in st.session_state:
            st.session_state.qa_history = []
        
        # Display chat history
        if st.session_state.qa_history:
            st.subheader("Conversation History")
            for qa in st.session_state.qa_history:
                with st.chat_message("user"):
                    st.write(qa['question'])
                with st.chat_message("assistant"):
                    st.write(qa['answer'])
        
        # Question input
        question = st.text_input(
            "Ask a question:",
            placeholder="e.g., What are the main challenges mentioned?",
            key="qa_input"
        )
        
        col1, col2 = st.columns([1, 5])
        with col1:
            ask_button = st.button("🤔 Ask", type="primary", use_container_width=True)
        with col2:
            if st.button("🗑️ Clear History", use_container_width=True):
                st.session_state.qa_history = []
                st.rerun()
        
        if ask_button and question:
            with st.spinner("🤔 Thinking..."):
                answer = st.session_state.nova_client.answer_question(
                    question=question,
                    context=st.session_state.current_research['synthesis']
                )
                
                # Save to history
                st.session_state.qa_history.append({
                    'question': question,
                    'answer': answer,
                    'timestamp': datetime.now().isoformat()
                })
                
                st.rerun()
        
        # Suggested questions
        with st.expander("💡 Suggested Questions"):
            suggestions = [
                "What are the key findings?",
                "What are the main challenges?",
                "What are the future implications?",
                "Are there any conflicting viewpoints?",
                "What are the practical applications?"
            ]
            for suggestion in suggestions:
                if st.button(suggestion, key=f"suggest_{suggestion}"):
                    st.session_state.qa_input = suggestion
                    st.rerun()
    
    else:
        st.info("👈 Complete a research query first to ask questions!")
        st.markdown("""
        ### How Q&A Works
        
        1. Complete a research query
        2. Ask any follow-up questions
        3. Nova AI answers based on your research context
        4. Build a conversation to dive deeper
        """)

with tab4:
    st.header("📈 Research Analytics")
    
    if st.session_state.research_history:
        # Overall stats
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Researches", len(st.session_state.research_history))
        with col2:
            total_sources = sum(len(r.get('sources', [])) for r in st.session_state.research_history)
            st.metric("Total Sources", total_sources)
        with col3:
            avg_sources = total_sources / len(st.session_state.research_history) if st.session_state.research_history else 0
            st.metric("Avg Sources/Research", f"{avg_sources:.1f}")
        with col4:
            qa_count = len(st.session_state.get('qa_history', []))
            st.metric("Questions Asked", qa_count)
        
        st.divider()
        
        # Research timeline
        st.subheader("📅 Research Timeline")
        timeline_data = []
        for r in st.session_state.research_history:
            timeline_data.append({
                'Date': r['timestamp'][:10],
                'Query': r['query'][:50],
                'Sources': len(r['sources'])
            })
        
        if timeline_data:
            fig = px.scatter(timeline_data, x='Date', y='Sources', 
                           hover_data=['Query'],
                           title='Research Activity Over Time',
                           size='Sources',
                           color='Sources')
            st.plotly_chart(fig, use_container_width=True)
        
        st.divider()
        
        # Topic analysis
        st.subheader("🏷️ Research Topics")
        all_queries = ' '.join([r['query'] for r in st.session_state.research_history])
        words = re.findall(r'\w+', all_queries.lower())
        common_topics = Counter([w for w in words if len(w) > 4])
        
        if common_topics:
            top_topics = dict(common_topics.most_common(15))
            fig = px.bar(x=list(top_topics.keys()), y=list(top_topics.values()),
                        title='Most Researched Topics',
                        labels={'x': 'Topic', 'y': 'Frequency'},
                        color=list(top_topics.values()),
                        color_continuous_scale='Blues')
            st.plotly_chart(fig, use_container_width=True)
        
        st.divider()
        
        # Recent activity
        st.subheader("🕐 Recent Activity")
        for i, research in enumerate(reversed(st.session_state.research_history[-10:])):
            with st.expander(f"{research['timestamp'][:19]} - {research['query'][:60]}"):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**Sources:** {len(research['sources'])}")
                    st.caption(research['synthesis'][:200] + "...")
                with col2:
                    if st.button("📖 View", key=f"view_{i}"):
                        st.session_state.current_research = research
                        st.rerun()
    
    else:
        st.info("📊 Complete some research to see analytics!")
        st.markdown("""
        ### Analytics Features
        
        - Track your research history
        - Visualize research patterns
        - Analyze topic trends
        - Monitor source usage
        - View activity timeline
        """)

# Footer
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("🔬 Nova Research Agent v1.0")
with col2:
    st.caption("Powered by Amazon Nova AI")
with col3:
    st.caption("🏆 Amazon Nova AI Hackathon 2026")
