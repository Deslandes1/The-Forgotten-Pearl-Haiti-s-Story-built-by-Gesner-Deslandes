import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="The Forgotten Pearl: Haiti's Story – built by Gesner Deslandes",
    page_icon="📖",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .lesson-card {
        background-color: #f8f9fa;
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .lesson-card:hover { transform: translateY(-5px); }
    .story-text {
        font-family: 'Georgia', serif;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #333;
        text-align: justify;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        background-color: #f1f1f1;
        border-radius: 20px;
    }
    .sidebar-logo {
        text-align: center;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .pulse-dot {
        display: inline-block;
        width: 12px;
        height: 12px;
        background-color: #ff4444;
        border-radius: 50%;
        animation: pulse 1.2s infinite;
        margin-right: 8px;
        vertical-align: middle;
    }
    @keyframes pulse {
        0% { transform: scale(0.8); opacity: 0.5; }
        50% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(0.8); opacity: 0.5; }
    }
    .reading-indicator {
        display: inline-flex;
        align-items: center;
        background: #f0f0f0;
        padding: 5px 12px;
        border-radius: 30px;
        font-size: 0.8rem;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown('<div class="sidebar-logo">📘</div>', unsafe_allow_html=True)
    st.markdown("## 🌐 GlobalInternet.py")
    st.markdown("**👨‍💻 Gesner Deslandes** – Storyteller & Python Builder")
    st.markdown("📞 (509) 4738-5663")
    st.markdown("✉️ deslandes78@gmail.com")
    st.markdown("---")
    st.markdown("🌍 [Visit our website](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown("### 📖 The Forgotten Pearl")
    st.markdown("20 lessons – Why Haiti is forgotten from the world")
    st.markdown("---")
    st.caption("Built by Gesner Deslandes – GlobalInternet.py")

# ---------- LESSONS DATA (with fixed, reliable image URLs) ----------
lessons = [
    {
        "title": "Lesson 1: The Pearl of the Caribbean",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&auto=format",
        "text": "Once upon a time, Haiti was called the Pearl of the Caribbean. Its sun was warm and inviting. Tourists came from all over the world to enjoy the golden beaches. They visited the old museums in Port‑au‑Prince. They stayed in beautiful hotels nestled in the countryside. The people welcomed visitors with open hearts. Music and laughter filled the streets every evening. Farmers sold fresh mangoes and coffee by the roadside. Artisans carved wooden sculptures that amazed everyone. The Citadelle stood proud on the mountaintop, a symbol of freedom. Haiti was the first black republic to abolish slavery. Its history inspired the world. But over the years, political storms began to gather. The pearl started to lose its shine. And slowly, the world began to forget.",
        "image_caption": "A beautiful Haitian beach at sunset"
    },
    {
        "title": "Lesson 2: A Land of Rich History",
        "image": "https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?w=600&auto=format",
        "text": "Haiti’s history is unlike any other. The Taino people lived there first, calling it Ayiti, land of high mountains. Then came the French, who brought slaves from Africa. The slaves rose up in a great rebellion led by Toussaint Louverture. They fought for twelve long years. In 1804, Haiti became the first free black republic in the world. The victory sent shockwaves across the Americas. Other nations feared that their own slaves would revolt. So they isolated Haiti, refusing to recognize its independence. They demanded a huge payment as compensation. For decades, Haiti paid France for its freedom. That debt crippled the young nation. Even today, that original injustice still echoes. Tourists once marveled at the Sans‑Souci Palace. They walked through the ruins of the Citadelle. But those wonders are now visited by only a few. The world forgot because it chose to look away.",
        "image_caption": "The Citadelle Laferrière – a symbol of Haitian freedom"
    },
    {
        "title": "Lesson 3: The Sun, the Sea and the Smiles",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&auto=format",
        "text": "I remember when I was a child, my family would take me to the beaches of Jacmel. The water was so clear you could see every fish. My mother would pack fried plantains and fresh oranges. My father would tell stories of the old days. Other families were there too, laughing and splashing. Everyone felt safe. The sun always shone, and the breeze carried the smell of salt. There were visitors from Canada, France and the United States. They danced to kompa music on the sand. They bought paintings from local artists. The hotel owners smiled because their rooms were full. The fishermen brought in fish to sell. Everyone earned a living. Those days were not perfect, but they were happy. Now, when I drive to the same beach, I see empty hotels. The sand is still there, but the tourists are gone. The smiles are harder to find. The world forgot what we had to offer.",
        "image_caption": "A quiet Haitian beach – still beautiful, but empty of visitors"
    },
    {
        "title": "Lesson 4: The First Cracks in the Pearl",
        "image": "https://images.unsplash.com/photo-1444464666168-49d633b86797?w=600&auto=format",
        "text": "The trouble did not begin overnight. It started with small cracks in the foundation. After the great earthquake of 2010, Haiti received billions of dollars in aid. Only a fraction reached the people who needed it. Empty promises were made by foreign organizations. New roads were planned but never built. Schools were promised but remained rubble. The government was weak and often corrupt. The people grew tired of waiting. Gangs began to take control of neighbourhoods. They offered safety and food where the state could not. Over time, those gangs grew stronger. Kidnappings for ransom became common. Businesses closed, and jobs disappeared. The middle class started to leave. The rich built high walls around their houses. The poor had nowhere to go. The cracks grew wider. The world watched but did nothing. By the time anyone noticed, the pearl had already shattered into pieces.",
        "image_caption": "Rubble after the 2010 earthquake – a turning point"
    },
    {
        "title": "Lesson 5: When the Tourists Stopped Coming",
        "image": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=600&auto=format",
        "text": "I worked as a guide at a small hotel in Cap‑Haïtien. Every morning, I would greet guests with a smile. They came from cruise ships that docked at the port. I showed them the Citadelle and the King's Palace. They loved the history and the views. The hotel had fifty rooms, and most nights they were full. I earned enough to help my mother and younger brother. Then the security situation began to change. Foreign governments issued travel warnings. The cruise ships stopped coming. The hotel closed its doors. I lost my job, just like hundreds of others. The restaurant next door closed too. The souvenir market became empty. The drivers who used to take tourists around had no work. We all watched the ships sail away to other islands. The Dominican Republic, Jamaica and Puerto Rico welcomed them. Haiti was left behind. The world did not stop traveling. It just traveled somewhere else. And Haiti became forgotten.",
        "image_caption": "Empty hotel pool – a sign of lost tourism"
    },
    {
        "title": "Lesson 6: The Pain of Inflation",
        "image": "https://images.unsplash.com/photo-1508615070457-7baeba4000b2?w=600&auto=format",
        "text": "Inflation is a word that many Haitians now know too well. Five years ago, a bag of rice cost 250 gourdes. Today, that same bag costs 1,200 gourdes. A small bottle of cooking oil has tripled in price. The market is full of food, but nobody can afford it. I see mothers counting coins to buy a few tomatoes. Fathers skip meals so their children can eat. The salary that once fed a family for a week now lasts only two days. People have stopped buying meat or eggs. They eat only rice and beans, sometimes not even that. The local currency has lost its value against the dollar. Those who receive money from abroad can survive. Those who depend on local work are struggling. I watch my neighbors sell furniture, then clothes, then hope. Inflation is like a slow fire. It does not burn you all at once. But one day you wake up, and everything you had is gone. The world does not feel this fire, so the world does not care.",
        "image_caption": "A market stall with goods that are too expensive"
    },
    {
        "title": "Lesson 7: Hunger That Never Leaves",
        "image": "https://images.unsplash.com/photo-1515960363144-d3eae8b1f7c6?w=600&auto=format",
        "text": "Hunger has become a permanent visitor in many homes. I remember when my grandmother would cook a large pot of soup joumou every Sunday. The whole family would gather to eat and laugh. Now, soup joumou is a luxury for the rich. Children go to school with empty stomachs. They faint in class because they have not eaten. Teachers use their own money to buy snacks. The World Food Program has reduced its aid. Local food production has fallen because farmers cannot buy seeds. The gangs control the roads, so food cannot reach the cities. In the countryside, people eat wild roots and leaves. In Port‑au‑Prince, families share one meal a day. I have seen babies who are too weak to cry. The hunger is not caused by a drought or a flood. It is caused by the collapse of a whole system. The world sends money occasionally, but it does not send justice. And without justice, the hungry cannot be fed.",
        "image_caption": "A child eating a simple plate of rice – hunger is everywhere"
    },
    {
        "title": "Lesson 8: Education Against All Odds",
        "image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=600&auto=format",
        "text": "Even in the darkest times, Haitian parents fight for their children's education. I know a mother who walks two hours each day to sell charcoal. She does it so her son can stay in school. His uniform is patched, but it is clean. His books are borrowed, but he reads them every night. The school has no windows and sometimes no roof. The teacher is paid very little, but she still comes. There are no computers or projectors. They learn by writing on small chalkboards. But the children are hungry to learn. They know that education is their only way out. Every year, many students pass the national exams against all odds. They dream of becoming doctors, engineers and teachers. Their families sacrifice everything to pay the small fees. The government does not help them. Foreign aid rarely reaches the classrooms. But the people do not give up. They know that a child with a book can change a family. They know that a nation that reads can raise itself. So they keep fighting, even when the world forgets them.",
        "image_caption": "Children learning in a humble classroom – hope still lives"
    },
    {
        "title": "Lesson 9: The Support of Family and Friends",
        "image": "https://images.unsplash.com/photo-1511632765486-a2d5c6ff58d0?w=600&auto=format",
        "text": "One thing that keeps Haiti alive is the solidarity among its people. When a family cannot pay for a funeral, the neighbours collect money. When a mother falls sick, her sister cooks for her children. When a young man wants to start a business, his friends lend him what they can. This is not charity. This is how we survive. I have seen a brother give his last gourde so his sister can buy medicine. I have seen cousins share one room so that a newly married couple can have privacy. Those who live abroad send money home every month. They call every Sunday to hear the news. They plan to return one day, when the country is safe. This network of love is our bank. It is our insurance. It is our hope. The world does not see this invisible system. It only sees the gangs, the poverty and the politics. But inside the homes, there are thousands of small acts of kindness. Those acts are the real treasure of Haiti. They cannot be stolen or bombed. They are what the world forgot to notice.",
        "image_caption": "A family gathering – solidarity keeps Haiti strong"
    },
    {
        "title": "Lesson 10: The President's Death – A Turning Point",
        "image": "https://images.unsplash.com/photo-1581089781785-603a5b6a5f4b?w=600&auto=format",
        "text": "The night of July 7, 2021, changed everything. President Jovenel Moïse was assassinated in his own bedroom. The whole country woke up to a nightmare. No one knew who had done it or why. The security forces were confused. Gangs took advantage of the chaos. They expanded into new neighbourhoods. Kidnappings, murders and looting increased every day. The economy, already weak, collapsed further. International investors ran away. Tourists had already left long before. Now even humanitarian workers began to leave. The government could not control the streets. The police were outnumbered and outgunned. The people felt abandoned. There was no president, no parliament, no justice. The gangs literally ran the country. That day marked the end of any hope for a quick recovery. The world condemned the assassination. But it offered no real help. Haiti was left to burn by itself. And the fire has not gone out since. The question remains: who benefited from this chaos? The answer is still unknown. But one day the truth will come out. Until then, the people pay the price every single day.",
        "image_caption": "A darkened presidential palace – symbol of a nation in crisis"
    },
    {
        "title": "Lesson 11: Living in the Grip of Insecurity",
        "image": "https://images.unsplash.com/photo-1542886369-9f0ded4b0bf4?w=600&auto=format",
        "text": "Insecurity has become a daily reality for every Haitian. I cannot walk to the market without fear of being kidnapped. My sister cannot drive to work because gangs have blocked the road. Children cannot play outside after noon. The sound of gunshots is more common than the sound of laughter. We have learned to identify which gang controls which street. We pay taxes to them, or we risk our lives. Some people have stopped going to church. Weddings and funerals are small, quick and silent. The schools close early to get children home before dark. We communicate by WhatsApp to know which roads are safe. Every day brings a new horror story. A neighbour taken from his car. A young girl shot because her father refused to pay a ransom. A driver burned alive in his bus. The police do not come. The army does not exist. We are alone with the gunmen. The world knows about our insecurity, but it does nothing. They send diplomatic notes and condemnations. They do not send soldiers or real help. So the gangs grow stronger, and we grow weaker. And the world keeps scrolling past our suffering.",
        "image_caption": "Armed men on a street – the daily reality of insecurity"
    },
    {
        "title": "Lesson 12: The Inflation Tax",
        "image": "https://images.unsplash.com/photo-1508615070457-7baeba4000b2?w=600&auto=format",
        "text": "Inflation is a silent thief that robs us every day. When the gourde loses value, our savings disappear. Those who worked for thirty years cannot retire. Their pension is worth nothing. Young people cannot save for a house or a wedding. They spend everything they earn on basic food. The price of imported rice, oil, and sugar goes up every week. Local products become more expensive too, because farmers cannot afford fuel. The baker cannot buy flour, so bread becomes a luxury. The cook cannot buy charcoal, so hot meals are rare. The mother cannot buy milk, so babies drink watered‑down porridge. Every time we go to the bank, the exchange rate is worse. People with dollars are kings. People with gourdes are beggars. The central bank tries to control inflation, but it is like holding back the ocean. The real cause is political instability and the flight of capital. The rich send their money abroad. The poor are left with worthless paper. This is not an economic crisis. It is a slow execution. The world sends food sometimes, but it does not send justice. So we pay the inflation tax every single day, and nobody helps us.",
        "image_caption": "A stack of local currency – losing value every day"
    },
    {
        "title": "Lesson 13: Despite Everything, We Laugh",
        "image": "https://images.unsplash.com/photo-1529619768549-0b1242d0a14c?w=600&auto=format",
        "text": "Even in the worst crisis, Haitians have not forgotten how to laugh. I watch my neighbors sit on their front steps in the evening and tell jokes. They make fun of the politicians and the gangs. They laugh at their own empty pockets. Laughter is a kind of medicine. It reminds us that we are still alive. On Sundays, some people still dress up and go to church. They sing loudly, as if they have no fear. Young people play football in the empty lots, even if they have no shoes. Mothers still braid their daughters' hair with colorful ribbons. Fathers still play dominoes with their friends. The radio still plays kompa, and sometimes we dance in the living room. We cannot let the gangs steal our joy. That would be a second death. So we choose to celebrate small things. A good meal. A safe night. A child who passed a test. A friend who returned from abroad. These moments are our treasure. The world does not see our laughter. It only sees the headlines. But our laughter is louder than the guns. And that is how we survive.",
        "image_caption": "Children playing in the street – joy still exists"
    },
    {
        "title": "Lesson 14: The Help From the Diaspora",
        "image": "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=600&auto=format",
        "text": "Every month, millions of dollars are sent home by Haitians living abroad. They work in factories in the Dominican Republic. They drive taxis in New York and Miami. They clean hospitals in Paris and Montreal. They left because they could not find work here. But they never forgot their families. The money they send pays for school fees, medical bills and funerals. It buys rice, oil and medicine. It fixes roofs and buys chickens. Without this help, half the country would starve. The diaspora is our lifeline. They also send clothes, shoes and toys. They pay for weddings and baptisms. They call every week to hear the voices of their parents. Some of them have saved for years to build a small house in their village. They dream of returning when the country is safe. They are the invisible hand that keeps Haiti standing. The world does not thank them. But we do. Every morning, we wake up because of them. Every night, we sleep because of them. The diaspora is the real hero of this story. And they will not let Haiti die.",
        "image_caption": "A money transfer shop – symbol of diaspora support"
    },
    {
        "title": "Lesson 15: A Glimmer of Calm",
        "image": "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=600&auto=format",
        "text": "In late 2025, something unexpected happened. The violence began to decrease. Some of the gangs walked away from their strongholds. Others moved to the countryside. The main roads became safer. People started to go out again to buy food. Children returned to school without fear. The markets filled with vendors. The police managed to arrest a few gang leaders. International pressure forced some countries to stop selling weapons to the gangs. The United Nations sent a small support mission. It was not perfect, but it helped. The calm did not come by accident. Many believe it was designed. Someone planned for the chaos to end at a certain time. Who benefited from the peace? The same people who benefited from the war? The answer is not yet known. The trial of those accused of the president's murder will begin soon. Many hope that the truth will come out. For now, we breathe a little easier. There is a glimmer of hope. But we have been disappointed before. So we wait and watch. The world may still forget us. But we will remember everything.",
        "image_caption": "A quiet street in Port‑au‑Prince – a sign of fragile calm"
    },
    {
        "title": "Lesson 16: The Search for Justice",
        "image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=600&auto=format",
        "text": "Justice is a word that Haitians have heard all their lives but rarely seen. The trial of those accused of killing President Moïse is a test. Will the powerful be held accountable? Or will they buy their freedom? The people watch the courts with tired eyes. They have seen too many cases postponed. Too many judges bribed. Too many witnesses killed. But this time feels different. There is international pressure. There are journalists watching. The families of the victims demand the truth. The young people in the streets chant for justice. They know that without it, the cycle will repeat. Another president will be killed. Another crisis will start. Another generation will suffer. So they march and they write and they pray. They send emails to foreign embassies. They post on social media. They will not let the truth be buried. The trial will happen, and the world is finally paying attention. It is a small step, but it is a step. If justice comes, Haiti might finally heal. If it does not, the people will know that the world has truly abandoned them. But they will still fight. Because fighting for justice is the only way to live.",
        "image_caption": "A courtroom – the hope for justice"
    },
    {
        "title": "Lesson 17: How Did We Get Here?",
        "image": "https://images.unsplash.com/photo-1454789548928-9efd52dc4031?w=600&auto=format",
        "text": "How did Haiti go from the Pearl of the Caribbean to a forgotten nation? Some say it began with the independence debt. Others point to the Duvalier dictatorships. Some blame the international community for decades of interference. Others say it is the fault of bad leaders. The truth is that many forces acted together. Foreign powers starved Haiti's economy. Local leaders stole the nation's money. Natural disasters broke its infrastructure. Gangs destroyed its safety. The world looked away because Haiti had no oil or gold to offer. There was no profit in helping. So the country fell. One stone after another, the wall collapsed. The people could not stop it. They were too poor, too weak, too divided. Now we are left with the rubble. The question is: can we rebuild? The answer depends on whether the world will finally see us. Not as a charity case, but as a nation of proud people. Not as a problem to be managed, but as a partner to be respected. We did not get here by accident. We got here because of choices made by the powerful. Those choices are not irreversible. But they will not be reversed unless the world remembers. And so far, the world has forgotten.",
        "image_caption": "A map of Haiti – asking why the pearl was lost"
    },
    {
        "title": "Lesson 18: The Role of the Media",
        "image": "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=600&auto=format",
        "text": "The international media has played a big role in Haiti's forgotten story. When disaster strikes, the cameras arrive. They show the dead bodies and the rubble. They interview the hungry children and the weeping mothers. Then, when the news cycle ends, the cameras leave. They do not stay to show the recovery. They do not report on the small victories. They do not tell the stories of the teachers who work without pay. They do not mention the artists who paint in the dark. The media sells tragedy, not hope. And so the world sees Haiti only as a place of sadness. People become numb to the images. They stop donating. They stop caring. Haiti becomes a background noise. This is how a country is forgotten. Not by silence, but by selective storytelling. The people of Haiti do not want pity. They want solidarity. They want the world to see their strength, not only their suffering. But the media does not broadcast strength. So the world remains ignorant. If you want to remember Haiti, you must look deeper than the headlines. You must listen to the stories that are not told. That is what this book tries to do.",
        "image_caption": "A news camera – how the world sees Haiti"
    },
    {
        "title": "Lesson 19: What Can Be Done?",
        "image": "https://images.unsplash.com/photo-1469571486292-0ba58a3f068b?w=600&auto=format",
        "text": "The situation in Haiti is desperate, but it is not hopeless. There are steps that can change everything. First, the international community must support a real security mission. Not with words, but with soldiers and money. Second, the Haitian government must be restructured. Corruption must be punished, not rewarded. Third, foreign investment must be encouraged in safe zones. Jobs will calm the anger of young people. Fourth, education must be funded. A literate population can build a stable nation. Fifth, agriculture must be modernised. Haiti can feed itself without foreign rice. Sixth, the diaspora must be invited to return with their skills. Seventh, the trial for the president's murder must be fair and transparent. Eighth, local governance must be strengthened. Ninth, the gangs must be disarmed by a serious force. Tenth, the world must change its view of Haiti. Not as a problem, but as a partner. These steps are not impossible. Other countries have risen from worse situations. But it will take will. It will take courage. And it will take the world remembering that Haiti still exists. We cannot do it alone. We need friends who do not run at the first sign of trouble. We need friends who will stay. Are you one of them? The future is still unwritten. Help us write a new chapter.",
        "image_caption": "Hands building a house – reconstruction is possible"
    },
    {
        "title": "Lesson 20: The Pearl Can Shine Again",
        "image": "https://images.unsplash.com/photo-1552152974-19b9c58a6387?w=600&auto=format",
        "text": "The Pearl of the Caribbean has been covered in dirt, but it is not destroyed. Under the rubble, there is still beauty. Under the fear, there is still courage. Under the hunger, there is still dignity. Haiti has risen before, and it can rise again. The young people I see every day give me hope. They learn coding on old laptops. They practice English by watching YouTube. They start small businesses with almost nothing. They organise neighbourhood watches to keep the gangs away. They are not waiting for the world to save them. They are saving themselves. But they need help. A hand up, not a handout. Investment, not pity. A chance, not a charity. If you are reading this, you have the power to be part of the solution. You can donate to Haitian organisations directly. You can pressure your government to support a real security mission. You can visit Haiti when it is safe, and tell the world what you see. You can share the true stories of Haiti, not just the tragedies. The pearl is still here. It is waiting for the light. Will you help us polish it? The story of Haiti is not over. The next chapter is being written right now. Let us make sure it is a story of hope, justice and rebirth. The world forgot Haiti. But Haiti has never forgotten itself. And we will not let you forget us again.",
        "image_caption": "A young Haitian artist painting – the pearl still shines from within"
    }
]

# ---------- MAIN PAGE ----------
def main():
    st.markdown(
        '<div class="main-header"><h1>📘 The Forgotten Pearl: Haiti\'s Story</h1><p>Book 1 – built by Gesner Deslandes · 20 lessons about why Haiti is forgotten from the world</p></div>',
        unsafe_allow_html=True
    )
    
    # Lesson selector in sidebar
    lesson_titles = [f"{i+1}. {lesson['title']}" for i, lesson in enumerate(lessons)]
    selected_idx = st.sidebar.selectbox("📖 Select Lesson", range(len(lessons)), format_func=lambda i: lesson_titles[i])
    
    lesson = lessons[selected_idx]
    
    # Display the lesson card
    with st.container():
        st.markdown(f'<div class="lesson-card">', unsafe_allow_html=True)
        col_img, col_text = st.columns([1, 2])
        with col_img:
            st.image(lesson['image'], caption=lesson.get('image_caption', 'Illustration'), use_container_width=True)
        with col_text:
            st.markdown(f"## {lesson['title']}")
            st.markdown(f'<div class="story-text">{lesson["text"]}</div>', unsafe_allow_html=True)
            
            # Read Aloud button with visual indicator
            read_btn = st.button(f"🔊 Read Aloud (Lesson {selected_idx+1})", key=f"read_{selected_idx}")
            if read_btn:
                # Show a pulsing indicator while audio is playing
                indicator = st.empty()
                indicator.markdown(
                    '<div class="reading-indicator"><span class="pulse-dot"></span> 🔊 Reading now... (audio playing)</div>',
                    unsafe_allow_html=True
                )
                # Escape special characters for JavaScript
                text_to_speak = lesson["text"].replace('"', '\\"').replace("\n", " ").replace("'", "\\'")
                js_code = f"""
                <script>
                    var utterance = new SpeechSynthesisUtterance("{text_to_speak}");
                    utterance.lang = "en-US";
                    utterance.onend = function() {{
                        // Notify Streamlit that speech has ended (optional)
                        var event = new CustomEvent('streamlit:setComponentValue', {{detail: {{value: "done"}}}});
                        window.dispatchEvent(event);
                    }};
                    window.speechSynthesis.cancel();
                    window.speechSynthesis.speak(utterance);
                </script>
                """
                components.html(js_code, height=0)
                # The indicator will stay until the user clicks another button or refreshes.
                # To auto‑clear after speech ends would require more complex JS.
                st.success("🔊 Now reading aloud... (make sure your device volume is on)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown(f"""
    <div class="footer">
        <p>© {datetime.now().year} GlobalInternet.py – Story Telling with Gesner Deslandes</p>
        <p>📖 "The Forgotten Pearl: Haiti's Story" – Book 1: Why Haiti is forgotten from the world<br>Built by Gesner Deslandes</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- PAGE ROUTING ----------
if __name__ == "__main__":
    main()
