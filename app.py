import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="The Forgotten Pearl: Haiti's Story – built by Gesner Deslandes",
    page_icon="📖",
    layout="wide"
)

# ---------- LANGUAGE STATE ----------
if "lang" not in st.session_state:
    st.session_state.lang = "en"

# ---------- TRANSLATIONS FOR UI ----------
ui_text = {
    "en": {
        "app_title": "📘 The Forgotten Pearl: Haiti's Story",
        "app_sub": "Book 1 – built by Gesner Deslandes · 20 lessons about why Haiti is forgotten from the world",
        "sidebar_logo": "📘",
        "sidebar_company": "🌐 GlobalInternet.py",
        "sidebar_founder": "👨‍💻 Gesner Deslandes – Storyteller & Python Builder",
        "sidebar_phone": "📞 (509) 4738-5663",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_website": "🌍 Visit our website",
        "sidebar_book_title": "📖 The Forgotten Pearl",
        "sidebar_book_desc": "20 lessons – Why Haiti is forgotten from the world",
        "sidebar_caption": "Built by Gesner Deslandes – GlobalInternet.py",
        "lesson_selector": "📖 Select Lesson",
        "read_aloud_button": "🔊 Read Aloud",
        "reading_indicator": "🔊 Reading now... (audio playing)",
        "reading_success": "🔊 Now reading aloud... (make sure your device volume is on)",
        "footer_copyright": "GlobalInternet.py – Story Telling with Gesner Deslandes",
        "footer_book": "📖 \"The Forgotten Pearl: Haiti's Story\" – Book 1: Why Haiti is forgotten from the world",
        "footer_built": "Built by Gesner Deslandes",
        "language_selector": "🌐 Language",
    },
    "fr": {
        "app_title": "📘 La Perle Oubliée : L’Histoire d’Haïti",
        "app_sub": "Livre 1 – construit par Gesner Deslandes · 20 leçons sur pourquoi Haïti est oubliée du monde",
        "sidebar_logo": "📘",
        "sidebar_company": "🌐 GlobalInternet.py",
        "sidebar_founder": "👨‍💻 Gesner Deslandes – Conteur & Constructeur Python",
        "sidebar_phone": "📞 (509) 4738-5663",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_website": "🌍 Visitez notre site web",
        "sidebar_book_title": "📖 La Perle Oubliée",
        "sidebar_book_desc": "20 leçons – Pourquoi Haïti est oubliée du monde",
        "sidebar_caption": "Construit par Gesner Deslandes – GlobalInternet.py",
        "lesson_selector": "📖 Choisir la leçon",
        "read_aloud_button": "🔊 Lire à voix haute",
        "reading_indicator": "🔊 Lecture en cours... (audio en cours)",
        "reading_success": "🔊 Lecture en cours... (vérifiez le volume de votre appareil)",
        "footer_copyright": "GlobalInternet.py – Contes avec Gesner Deslandes",
        "footer_book": "📖 \"La Perle Oubliée : L’Histoire d’Haïti\" – Livre 1 : Pourquoi Haïti est oubliée du monde",
        "footer_built": "Construit par Gesner Deslandes",
        "language_selector": "🌐 Langue",
    },
    "es": {
        "app_title": "📘 La Perla Olvidada: La Historia de Haití",
        "app_sub": "Libro 1 – construido por Gesner Deslandes · 20 lecciones sobre por qué Haití es olvidada por el mundo",
        "sidebar_logo": "📘",
        "sidebar_company": "🌐 GlobalInternet.py",
        "sidebar_founder": "👨‍💻 Gesner Deslandes – Narrador & Constructor Python",
        "sidebar_phone": "📞 (509) 4738-5663",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_website": "🌍 Visite nuestro sitio web",
        "sidebar_book_title": "📖 La Perla Olvidada",
        "sidebar_book_desc": "20 lecciones – Por qué Haití es olvidada por el mundo",
        "sidebar_caption": "Construido por Gesner Deslandes – GlobalInternet.py",
        "lesson_selector": "📖 Seleccionar lección",
        "read_aloud_button": "🔊 Leer en voz alta",
        "reading_indicator": "🔊 Leyendo ahora... (audio en curso)",
        "reading_success": "🔊 Leyendo en voz alta... (asegúrese de que el volumen de su dispositivo esté activado)",
        "footer_copyright": "GlobalInternet.py – Narración con Gesner Deslandes",
        "footer_book": "📖 \"La Perla Olvidada: La Historia de Haití\" – Libro 1: Por qué Haití es olvidada por el mundo",
        "footer_built": "Construido por Gesner Deslandes",
        "language_selector": "🌐 Idioma",
    }
}

def _(key):
    return ui_text[st.session_state.lang].get(key, key)

# ---------- LESSONS DATA (ENGLISH) ----------
lessons_en = [
    {
        "title": "Lesson 1: The Pearl of the Caribbean",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&auto=format",
        "text": "Once upon a time, Haiti was called the Pearl of the Caribbean. Its sun was warm and inviting. Tourists came from all over the world to enjoy the golden beaches. They visited the old museums in Port‑au‑Prince. They stayed in beautiful hotels nestled in the countryside. The people welcomed visitors with open hearts. Music and laughter filled the streets every evening. Farmers sold fresh mangoes and coffee by the roadside. Artisans carved wooden sculptures that amazed everyone. The Citadelle stood proud on the mountaintop, a symbol of freedom. Haiti was the first black republic to abolish slavery. Its history inspired the world. But over the years, political storms began to gather. The pearl started to lose its shine. And slowly, the world began to forget.",
        "caption": "A beautiful Haitian beach at sunset"
    },
    {
        "title": "Lesson 2: A Land of Rich History",
        "image": "https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?w=600&auto=format",
        "text": "Haiti’s history is unlike any other. The Taino people lived there first, calling it Ayiti, land of high mountains. Then came the French, who brought slaves from Africa. The slaves rose up in a great rebellion led by Toussaint Louverture. They fought for twelve long years. In 1804, Haiti became the first free black republic in the world. The victory sent shockwaves across the Americas. Other nations feared that their own slaves would revolt. So they isolated Haiti, refusing to recognize its independence. They demanded a huge payment as compensation. For decades, Haiti paid France for its freedom. That debt crippled the young nation. Even today, that original injustice still echoes. Tourists once marveled at the Sans‑Souci Palace. They walked through the ruins of the Citadelle. But those wonders are now visited by only a few. The world forgot because it chose to look away.",
        "caption": "The Citadelle Laferrière – a symbol of Haitian freedom"
    },
    {
        "title": "Lesson 3: The Sun, the Sea and the Smiles",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&auto=format",
        "text": "I remember when I was a child, my family would take me to the beaches of Jacmel. The water was so clear you could see every fish. My mother would pack fried plantains and fresh oranges. My father would tell stories of the old days. Other families were there too, laughing and splashing. Everyone felt safe. The sun always shone, and the breeze carried the smell of salt. There were visitors from Canada, France and the United States. They danced to kompa music on the sand. They bought paintings from local artists. The hotel owners smiled because their rooms were full. The fishermen brought in fish to sell. Everyone earned a living. Those days were not perfect, but they were happy. Now, when I drive to the same beach, I see empty hotels. The sand is still there, but the tourists are gone. The smiles are harder to find. The world forgot what we had to offer.",
        "caption": "A quiet Haitian beach – still beautiful, but empty of visitors"
    },
    {
        "title": "Lesson 4: The First Cracks in the Pearl",
        "image": "https://images.unsplash.com/photo-1444464666168-49d633b86797?w=600&auto=format",
        "text": "The trouble did not begin overnight. It started with small cracks in the foundation. After the great earthquake of 2010, Haiti received billions of dollars in aid. Only a fraction reached the people who needed it. Empty promises were made by foreign organizations. New roads were planned but never built. Schools were promised but remained rubble. The government was weak and often corrupt. The people grew tired of waiting. Gangs began to take control of neighbourhoods. They offered safety and food where the state could not. Over time, those gangs grew stronger. Kidnappings for ransom became common. Businesses closed, and jobs disappeared. The middle class started to leave. The rich built high walls around their houses. The poor had nowhere to go. The cracks grew wider. The world watched but did nothing. By the time anyone noticed, the pearl had already shattered into pieces.",
        "caption": "Rubble after the 2010 earthquake – a turning point"
    },
    {
        "title": "Lesson 5: When the Tourists Stopped Coming",
        "image": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=600&auto=format",
        "text": "I worked as a guide at a small hotel in Cap‑Haïtien. Every morning, I would greet guests with a smile. They came from cruise ships that docked at the port. I showed them the Citadelle and the King's Palace. They loved the history and the views. The hotel had fifty rooms, and most nights they were full. I earned enough to help my mother and younger brother. Then the security situation began to change. Foreign governments issued travel warnings. The cruise ships stopped coming. The hotel closed its doors. I lost my job, just like hundreds of others. The restaurant next door closed too. The souvenir market became empty. The drivers who used to take tourists around had no work. We all watched the ships sail away to other islands. The Dominican Republic, Jamaica and Puerto Rico welcomed them. Haiti was left behind. The world did not stop traveling. It just traveled somewhere else. And Haiti became forgotten.",
        "caption": "Empty hotel pool – a sign of lost tourism"
    },
    {
        "title": "Lesson 6: The Pain of Inflation",
        "image": "https://images.unsplash.com/photo-1508615070457-7baeba4000b2?w=600&auto=format",
        "text": "Inflation is a word that many Haitians now know too well. Five years ago, a bag of rice cost 250 gourdes. Today, that same bag costs 1,200 gourdes. A small bottle of cooking oil has tripled in price. The market is full of food, but nobody can afford it. I see mothers counting coins to buy a few tomatoes. Fathers skip meals so their children can eat. The salary that once fed a family for a week now lasts only two days. People have stopped buying meat or eggs. They eat only rice and beans, sometimes not even that. The local currency has lost its value against the dollar. Those who receive money from abroad can survive. Those who depend on local work are struggling. I watch my neighbors sell furniture, then clothes, then hope. Inflation is like a slow fire. It does not burn you all at once. But one day you wake up, and everything you had is gone. The world does not feel this fire, so the world does not care.",
        "caption": "A market stall with goods that are too expensive"
    },
    {
        "title": "Lesson 7: Hunger That Never Leaves",
        "image": "https://images.unsplash.com/photo-1515960363144-d3eae8b1f7c6?w=600&auto=format",
        "text": "Hunger has become a permanent visitor in many homes. I remember when my grandmother would cook a large pot of soup joumou every Sunday. The whole family would gather to eat and laugh. Now, soup joumou is a luxury for the rich. Children go to school with empty stomachs. They faint in class because they have not eaten. Teachers use their own money to buy snacks. The World Food Program has reduced its aid. Local food production has fallen because farmers cannot buy seeds. The gangs control the roads, so food cannot reach the cities. In the countryside, people eat wild roots and leaves. In Port‑au‑Prince, families share one meal a day. I have seen babies who are too weak to cry. The hunger is not caused by a drought or a flood. It is caused by the collapse of a whole system. The world sends money occasionally, but it does not send justice. And without justice, the hungry cannot be fed.",
        "caption": "A child eating a simple plate of rice – hunger is everywhere"
    },
    {
        "title": "Lesson 8: Education Against All Odds",
        "image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=600&auto=format",
        "text": "Even in the darkest times, Haitian parents fight for their children's education. I know a mother who walks two hours each day to sell charcoal. She does it so her son can stay in school. His uniform is patched, but it is clean. His books are borrowed, but he reads them every night. The school has no windows and sometimes no roof. The teacher is paid very little, but she still comes. There are no computers or projectors. They learn by writing on small chalkboards. But the children are hungry to learn. They know that education is their only way out. Every year, many students pass the national exams against all odds. They dream of becoming doctors, engineers and teachers. Their families sacrifice everything to pay the small fees. The government does not help them. Foreign aid rarely reaches the classrooms. But the people do not give up. They know that a child with a book can change a family. They know that a nation that reads can raise itself. So they keep fighting, even when the world forgets them.",
        "caption": "Children learning in a humble classroom – hope still lives"
    },
    {
        "title": "Lesson 9: The Support of Family and Friends",
        "image": "https://images.unsplash.com/photo-1511632765486-a2d5c6ff58d0?w=600&auto=format",
        "text": "One thing that keeps Haiti alive is the solidarity among its people. When a family cannot pay for a funeral, the neighbours collect money. When a mother falls sick, her sister cooks for her children. When a young man wants to start a business, his friends lend him what they can. This is not charity. This is how we survive. I have seen a brother give his last gourde so his sister can buy medicine. I have seen cousins share one room so that a newly married couple can have privacy. Those who live abroad send money home every month. They call every Sunday to hear the news. They plan to return one day, when the country is safe. This network of love is our bank. It is our insurance. It is our hope. The world does not see this invisible system. It only sees the gangs, the poverty and the politics. But inside the homes, there are thousands of small acts of kindness. Those acts are the real treasure of Haiti. They cannot be stolen or bombed. They are what the world forgot to notice.",
        "caption": "A family gathering – solidarity keeps Haiti strong"
    },
    {
        "title": "Lesson 10: The President's Death – A Turning Point",
        "image": "https://images.unsplash.com/photo-1581089781785-603a5b6a5f4b?w=600&auto=format",
        "text": "The night of July 7, 2021, changed everything. President Jovenel Moïse was assassinated in his own bedroom. The whole country woke up to a nightmare. No one knew who had done it or why. The security forces were confused. Gangs took advantage of the chaos. They expanded into new neighbourhoods. Kidnappings, murders and looting increased every day. The economy, already weak, collapsed further. International investors ran away. Tourists had already left long before. Now even humanitarian workers began to leave. The government could not control the streets. The police were outnumbered and outgunned. The people felt abandoned. There was no president, no parliament, no justice. The gangs literally ran the country. That day marked the end of any hope for a quick recovery. The world condemned the assassination. But it offered no real help. Haiti was left to burn by itself. And the fire has not gone out since. The question remains: who benefited from this chaos? The answer is still unknown. But one day the truth will come out. Until then, the people pay the price every single day.",
        "caption": "A darkened presidential palace – symbol of a nation in crisis"
    },
    {
        "title": "Lesson 11: Living in the Grip of Insecurity",
        "image": "https://images.unsplash.com/photo-1542886369-9f0ded4b0bf4?w=600&auto=format",
        "text": "Insecurity has become a daily reality for every Haitian. I cannot walk to the market without fear of being kidnapped. My sister cannot drive to work because gangs have blocked the road. Children cannot play outside after noon. The sound of gunshots is more common than the sound of laughter. We have learned to identify which gang controls which street. We pay taxes to them, or we risk our lives. Some people have stopped going to church. Weddings and funerals are small, quick and silent. The schools close early to get children home before dark. We communicate by WhatsApp to know which roads are safe. Every day brings a new horror story. A neighbour taken from his car. A young girl shot because her father refused to pay a ransom. A driver burned alive in his bus. The police do not come. The army does not exist. We are alone with the gunmen. The world knows about our insecurity, but it does nothing. They send diplomatic notes and condemnations. They do not send soldiers or real help. So the gangs grow stronger, and we grow weaker. And the world keeps scrolling past our suffering.",
        "caption": "Armed men on a street – the daily reality of insecurity"
    },
    {
        "title": "Lesson 12: The Inflation Tax",
        "image": "https://images.unsplash.com/photo-1508615070457-7baeba4000b2?w=600&auto=format",
        "text": "Inflation is a silent thief that robs us every day. When the gourde loses value, our savings disappear. Those who worked for thirty years cannot retire. Their pension is worth nothing. Young people cannot save for a house or a wedding. They spend everything they earn on basic food. The price of imported rice, oil, and sugar goes up every week. Local products become more expensive too, because farmers cannot afford fuel. The baker cannot buy flour, so bread becomes a luxury. The cook cannot buy charcoal, so hot meals are rare. The mother cannot buy milk, so babies drink watered‑down porridge. Every time we go to the bank, the exchange rate is worse. People with dollars are kings. People with gourdes are beggars. The central bank tries to control inflation, but it is like holding back the ocean. The real cause is political instability and the flight of capital. The rich send their money abroad. The poor are left with worthless paper. This is not an economic crisis. It is a slow execution. The world sends food sometimes, but it does not send justice. So we pay the inflation tax every single day, and nobody helps us.",
        "caption": "A stack of local currency – losing value every day"
    },
    {
        "title": "Lesson 13: Despite Everything, We Laugh",
        "image": "https://images.unsplash.com/photo-1529619768549-0b1242d0a14c?w=600&auto=format",
        "text": "Even in the worst crisis, Haitians have not forgotten how to laugh. I watch my neighbors sit on their front steps in the evening and tell jokes. They make fun of the politicians and the gangs. They laugh at their own empty pockets. Laughter is a kind of medicine. It reminds us that we are still alive. On Sundays, some people still dress up and go to church. They sing loudly, as if they have no fear. Young people play football in the empty lots, even if they have no shoes. Mothers still braid their daughters' hair with colorful ribbons. Fathers still play dominoes with their friends. The radio still plays kompa, and sometimes we dance in the living room. We cannot let the gangs steal our joy. That would be a second death. So we choose to celebrate small things. A good meal. A safe night. A child who passed a test. A friend who returned from abroad. These moments are our treasure. The world does not see our laughter. It only sees the headlines. But our laughter is louder than the guns. And that is how we survive.",
        "caption": "Children playing in the street – joy still exists"
    },
    {
        "title": "Lesson 14: The Help From the Diaspora",
        "image": "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=600&auto=format",
        "text": "Every month, millions of dollars are sent home by Haitians living abroad. They work in factories in the Dominican Republic. They drive taxis in New York and Miami. They clean hospitals in Paris and Montreal. They left because they could not find work here. But they never forgot their families. The money they send pays for school fees, medical bills and funerals. It buys rice, oil and medicine. It fixes roofs and buys chickens. Without this help, half the country would starve. The diaspora is our lifeline. They also send clothes, shoes and toys. They pay for weddings and baptisms. They call every week to hear the voices of their parents. Some of them have saved for years to build a small house in their village. They dream of returning when the country is safe. They are the invisible hand that keeps Haiti standing. The world does not thank them. But we do. Every morning, we wake up because of them. Every night, we sleep because of them. The diaspora is the real hero of this story. And they will not let Haiti die.",
        "caption": "A money transfer shop – symbol of diaspora support"
    },
    {
        "title": "Lesson 15: A Glimmer of Calm",
        "image": "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=600&auto=format",
        "text": "In late 2025, something unexpected happened. The violence began to decrease. Some of the gangs walked away from their strongholds. Others moved to the countryside. The main roads became safer. People started to go out again to buy food. Children returned to school without fear. The markets filled with vendors. The police managed to arrest a few gang leaders. International pressure forced some countries to stop selling weapons to the gangs. The United Nations sent a small support mission. It was not perfect, but it helped. The calm did not come by accident. Many believe it was designed. Someone planned for the chaos to end at a certain time. Who benefited from the peace? The same people who benefited from the war? The answer is not yet known. The trial of those accused of the president's murder will begin soon. Many hope that the truth will come out. For now, we breathe a little easier. There is a glimmer of hope. But we have been disappointed before. So we wait and watch. The world may still forget us. But we will remember everything.",
        "caption": "A quiet street in Port‑au‑Prince – a sign of fragile calm"
    },
    {
        "title": "Lesson 16: The Search for Justice",
        "image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=600&auto=format",
        "text": "Justice is a word that Haitians have heard all their lives but rarely seen. The trial of those accused of killing President Moïse is a test. Will the powerful be held accountable? Or will they buy their freedom? The people watch the courts with tired eyes. They have seen too many cases postponed. Too many judges bribed. Too many witnesses killed. But this time feels different. There is international pressure. There are journalists watching. The families of the victims demand the truth. The young people in the streets chant for justice. They know that without it, the cycle will repeat. Another president will be killed. Another crisis will start. Another generation will suffer. So they march and they write and they pray. They send emails to foreign embassies. They post on social media. They will not let the truth be buried. The trial will happen, and the world is finally paying attention. It is a small step, but it is a step. If justice comes, Haiti might finally heal. If it does not, the people will know that the world has truly abandoned them. But they will still fight. Because fighting for justice is the only way to live.",
        "caption": "A courtroom – the hope for justice"
    },
    {
        "title": "Lesson 17: How Did We Get Here?",
        "image": "https://images.unsplash.com/photo-1454789548928-9efd52dc4031?w=600&auto=format",
        "text": "How did Haiti go from the Pearl of the Caribbean to a forgotten nation? Some say it began with the independence debt. Others point to the Duvalier dictatorships. Some blame the international community for decades of interference. Others say it is the fault of bad leaders. The truth is that many forces acted together. Foreign powers starved Haiti's economy. Local leaders stole the nation's money. Natural disasters broke its infrastructure. Gangs destroyed its safety. The world looked away because Haiti had no oil or gold to offer. There was no profit in helping. So the country fell. One stone after another, the wall collapsed. The people could not stop it. They were too poor, too weak, too divided. Now we are left with the rubble. The question is: can we rebuild? The answer depends on whether the world will finally see us. Not as a charity case, but as a nation of proud people. Not as a problem to be managed, but as a partner to be respected. We did not get here by accident. We got here because of choices made by the powerful. Those choices are not irreversible. But they will not be reversed unless the world remembers. And so far, the world has forgotten.",
        "caption": "A map of Haiti – asking why the pearl was lost"
    },
    {
        "title": "Lesson 18: The Role of the Media",
        "image": "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=600&auto=format",
        "text": "The international media has played a big role in Haiti's forgotten story. When disaster strikes, the cameras arrive. They show the dead bodies and the rubble. They interview the hungry children and the weeping mothers. Then, when the news cycle ends, the cameras leave. They do not stay to show the recovery. They do not report on the small victories. They do not tell the stories of the teachers who work without pay. They do not mention the artists who paint in the dark. The media sells tragedy, not hope. And so the world sees Haiti only as a place of sadness. People become numb to the images. They stop donating. They stop caring. Haiti becomes a background noise. This is how a country is forgotten. Not by silence, but by selective storytelling. The people of Haiti do not want pity. They want solidarity. They want the world to see their strength, not only their suffering. But the media does not broadcast strength. So the world remains ignorant. If you want to remember Haiti, you must look deeper than the headlines. You must listen to the stories that are not told. That is what this book tries to do.",
        "caption": "A news camera – how the world sees Haiti"
    },
    {
        "title": "Lesson 19: What Can Be Done?",
        "image": "https://images.unsplash.com/photo-1469571486292-0ba58a3f068b?w=600&auto=format",
        "text": "The situation in Haiti is desperate, but it is not hopeless. There are steps that can change everything. First, the international community must support a real security mission. Not with words, but with soldiers and money. Second, the Haitian government must be restructured. Corruption must be punished, not rewarded. Third, foreign investment must be encouraged in safe zones. Jobs will calm the anger of young people. Fourth, education must be funded. A literate population can build a stable nation. Fifth, agriculture must be modernised. Haiti can feed itself without foreign rice. Sixth, the diaspora must be invited to return with their skills. Seventh, the trial for the president's murder must be fair and transparent. Eighth, local governance must be strengthened. Ninth, the gangs must be disarmed by a serious force. Tenth, the world must change its view of Haiti. Not as a problem, but as a partner. These steps are not impossible. Other countries have risen from worse situations. But it will take will. It will take courage. And it will take the world remembering that Haiti still exists. We cannot do it alone. We need friends who do not run at the first sign of trouble. We need friends who will stay. Are you one of them? The future is still unwritten. Help us write a new chapter.",
        "caption": "Hands building a house – reconstruction is possible"
    },
    {
        "title": "Lesson 20: The Pearl Can Shine Again",
        "image": "https://images.unsplash.com/photo-1552152974-19b9c58a6387?w=600&auto=format",
        "text": "The Pearl of the Caribbean has been covered in dirt, but it is not destroyed. Under the rubble, there is still beauty. Under the fear, there is still courage. Under the hunger, there is still dignity. Haiti has risen before, and it can rise again. The young people I see every day give me hope. They learn coding on old laptops. They practice English by watching YouTube. They start small businesses with almost nothing. They organise neighbourhood watches to keep the gangs away. They are not waiting for the world to save them. They are saving themselves. But they need help. A hand up, not a handout. Investment, not pity. A chance, not a charity. If you are reading this, you have the power to be part of the solution. You can donate to Haitian organisations directly. You can pressure your government to support a real security mission. You can visit Haiti when it is safe, and tell the world what you see. You can share the true stories of Haiti, not just the tragedies. The pearl is still here. It is waiting for the light. Will you help us polish it? The story of Haiti is not over. The next chapter is being written right now. Let us make sure it is a story of hope, justice and rebirth. The world forgot Haiti. But Haiti has never forgotten itself. And we will not let you forget us again.",
        "caption": "A young Haitian artist painting – the pearl still shines from within"
    }
]

# ---------- FRENCH TRANSLATIONS ----------
lessons_fr = [
    {
        "title": "Leçon 1 : La Perle des Caraïbes",
        "image": lessons_en[0]["image"],
        "text": "Il était une fois, Haïti était appelée la Perle des Caraïbes. Son soleil était chaud et accueillant. Des touristes venaient du monde entier pour profiter des plages dorées. Ils visitaient les vieux musées de Port‑au‑Prince. Ils séjournaient dans de beaux hôtels nichés dans la campagne. Les gens accueillaient les visiteurs avec cœur. La musique et les rires remplissaient les rues chaque soir. Les agriculteurs vendaient des mangues fraîches et du café au bord des routes. Les artisans sculptaient des œuvres en bois qui émerveillaient tout le monde. La Citadelle se dressait fièrement au sommet de la montagne, symbole de liberté. Haïti a été la première république noire à abolir l'esclavage. Son histoire a inspiré le monde. Mais au fil des années, les tempêtes politiques ont commencé à se rassembler. La perle a commencé à perdre son éclat. Et lentement, le monde a commencé à oublier.",
        "caption": "Une belle plage haïtienne au coucher du soleil"
    },
    {
        "title": "Leçon 2 : Une terre de riche histoire",
        "image": lessons_en[1]["image"],
        "text": "L’histoire d’Haïti ne ressemble à aucune autre. Les Taïnos y vivaient en premier, l’appelant Ayiti, terre de hautes montagnes. Puis vinrent les Français, qui amenèrent des esclaves d’Afrique. Les esclaves se soulevèrent lors d’une grande rébellion menée par Toussaint Louverture. Ils se sont battus pendant douze longues années. En 1804, Haïti devient la première république noire libre du monde. La victoire a provoqué des ondes de choc dans toutes les Amériques. D’autres nations craignaient que leurs propres esclaves ne se révoltent. Ils ont donc isolé Haïti, refusant de reconnaître son indépendance. Ils ont exigé un paiement énorme en compensation. Pendant des décennies, Haïti a payé à la France sa liberté. Cette dette a paralysé la jeune nation. Encore aujourd’hui, cette injustice originelle résonne. Les touristes admiraient autrefois le palais Sans‑Souci. Ils parcouraient les ruines de la Citadelle. Mais ces merveilles ne sont plus visitées que par quelques-uns. Le monde a oublié parce qu’il a choisi de détourner le regard.",
        "caption": "La Citadelle Laferrière – un symbole de la liberté haïtienne"
    },
    {
        "title": "Leçon 3 : Le soleil, la mer et les sourires",
        "image": lessons_en[2]["image"],
        "text": "Je me souviens quand j’étais enfant, ma famille m’emmenait sur les plages de Jacmel. L’eau était si claire que l’on voyait chaque poisson. Ma mère préparait des bananes plantains frites et des oranges fraîches. Mon père racontait des histoires du bon vieux temps. D’autres familles étaient aussi là, riant et barbotant. Tout le monde se sentait en sécurité. Le soleil brillait toujours, et la brise apportait une odeur de sel. Il y avait des visiteurs du Canada, de France et des États‑Unis. Ils dansaient sur la musique kompa sur le sable. Ils achetaient des tableaux à des artistes locaux. Les hôteliers souriaient parce que leurs chambres étaient pleines. Les pêcheurs ramenaient du poisson à vendre. Tout le monde gagnait sa vie. Ces jours n’étaient pas parfaits, mais ils étaient heureux. Aujourd’hui, quand je conduis vers la même plage, je vois des hôtels vides. Le sable est toujours là, mais les touristes ont disparu. Les sourires sont plus difficiles à trouver. Le monde a oublié ce que nous avions à offrir.",
        "caption": "Une plage haïtienne tranquille – toujours belle, mais vide de visiteurs"
    },
    {
        "title": "Leçon 4 : Les premières fissures dans la Perle",
        "image": lessons_en[3]["image"],
        "text": "Les ennuis n’ont pas commencé du jour au lendemain. Cela a commencé par de petites fissures dans les fondations. Après le grand tremblement de terre de 2010, Haïti a reçu des milliards de dollars d’aide. Seule une fraction est parvenue aux personnes qui en avaient besoin. Des promesses creuses ont été faites par des organisations étrangères. De nouvelles routes ont été planifiées mais jamais construites. Des écoles ont été promises mais sont restées en ruines. Le gouvernement était faible et souvent corrompu. Les gens se sont lassés d’attendre. Des gangs ont commencé à prendre le contrôle de quartiers. Ils offraient sécurité et nourriture là où l’État ne pouvait pas. Au fil du temps, ces gangs sont devenus plus forts. Les enlèvements contre rançon sont devenus monnaie courante. Les entreprises ont fermé, les emplois ont disparu. La classe moyenne a commencé à partir. Les riches ont construit de hauts murs autour de leurs maisons. Les pauvres n’avaient nulle part où aller. Les fissures se sont élargies. Le monde a regardé sans rien faire. Quand quelqu’un a finalement remarqué, la perle était déjà en miettes.",
        "caption": "Décombres après le séisme de 2010 – un tournant"
    },
    {
        "title": "Leçon 5 : Quand les touristes ont cessé de venir",
        "image": lessons_en[4]["image"],
        "text": "Je travaillais comme guide dans un petit hôtel au Cap‑Haïtien. Chaque matin, j’accueillais les clients avec le sourire. Ils venaient de bateaux de croisière qui accostaient au port. Je leur montrais la Citadelle et le Palais du Roi. Ils adoraient l’histoire et les points de vue. L’hôtel avait cinquante chambres, et la plupart des nuits elles étaient pleines. Je gagnais assez pour aider ma mère et mon jeune frère. Puis la situation sécuritaire a commencé à changer. Les gouvernements étrangers ont émis des avertissements aux voyageurs. Les bateaux de croisière ont cessé de venir. L’hôtel a fermé ses portes. J’ai perdu mon emploi, comme des centaines d’autres. Le restaurant d’à côté a également fermé. Le marché de souvenirs est devenu vide. Les chauffeurs qui transportaient les touristes n’avaient plus de travail. Nous avons tous regardé les bateaux s’éloigner vers d’autres îles. La République dominicaine, la Jamaïque et Porto Rico les ont accueillis. Haïti a été laissé pour compte. Le monde n’a pas arrêté de voyager. Il a simplement voyagé ailleurs. Et Haïti est devenu oublié.",
        "caption": "Piscine d’hôtel vide – signe d’un tourisme perdu"
    },
    {
        "title": "Leçon 6 : La douleur de l’inflation",
        "image": lessons_en[5]["image"],
        "text": "L’inflation est un mot que beaucoup d’Haïtiens connaissent désormais trop bien. Il y a cinq ans, un sac de riz coûtait 250 gourdes. Aujourd’hui, ce même sac coûte 1 200 gourdes. Une petite bouteille d’huile de cuisson a triplé de prix. Le marché est plein de nourriture, mais personne ne peut se la permettre. Je vois des mères compter des pièces pour acheter quelques tomates. Les pères sautent des repas pour que leurs enfants puissent manger. Le salaire qui nourrissait autrefois une famille pendant une semaine ne dure plus que deux jours. Les gens ont arrêté d’acheter de la viande ou des œufs. Ils ne mangent que du riz et des haricots, parfois même pas cela. La monnaie locale a perdu sa valeur face au dollar. Ceux qui reçoivent de l’argent de l’étranger peuvent survivre. Ceux qui dépendent du travail local luttent. Je regarde mes voisins vendre leurs meubles, puis leurs vêtements, puis l’espoir. L’inflation est comme un feu lent. Il ne vous brûle pas tout d’un coup. Mais un jour vous vous réveillez, et tout ce que vous aviez a disparu. Le monde ne ressent pas ce feu, donc le monde s’en fiche.",
        "caption": "Un étal de marché avec des marchandises trop chères"
    },
    {
        "title": "Leçon 7 : La faim qui ne part jamais",
        "image": lessons_en[6]["image"],
        "text": "La faim est devenue un visiteur permanent dans de nombreux foyers. Je me souviens quand ma grand‑mère cuisinait une grande marmite de soupe joumou chaque dimanche. Toute la famille se rassemblait pour manger et rire. Aujourd’hui, la soupe joumou est un luxe réservé aux riches. Les enfants vont à l’école le ventre vide. Ils s’évanouissent en classe parce qu’ils n’ont pas mangé. Les enseignants utilisent leur propre argent pour acheter des collations. Le Programme alimentaire mondial a réduit son aide. La production alimentaire locale a chuté car les agriculteurs ne peuvent pas acheter de semences. Les gangs contrôlent les routes, donc la nourriture ne peut pas atteindre les villes. Dans les campagnes, les gens mangent des racines sauvages et des feuilles. À Port‑au‑Prince, les familles partagent un repas par jour. J’ai vu des bébés trop faibles pour pleurer. La faim n’est pas causée par une sécheresse ou une inondation. Elle est causée par l’effondrement de tout un système. Le monde envoie de l’argent de temps en temps, mais il n’envoie pas la justice. Et sans justice, les affamés ne peuvent être nourris.",
        "caption": "Un enfant mangeant une simple assiette de riz – la faim est partout"
    },
    {
        "title": "Leçon 8 : L’éducation contre vents et marées",
        "image": lessons_en[7]["image"],
        "text": "Même dans les moments les plus sombres, les parents haïtiens se battent pour l’éducation de leurs enfants. Je connais une mère qui marche deux heures chaque jour pour vendre du charbon de bois. Elle le fait pour que son fils puisse rester à l’école. Son uniforme est rapiécé, mais il est propre. Ses livres sont empruntés, mais il les lit chaque nuit. L’école n’a pas de fenêtres et parfois pas de toit. L’enseignante est très peu payée, mais elle vient quand même. Il n’y a ni ordinateurs ni projecteurs. Ils apprennent en écrivant sur de petits tableaux noirs. Mais les enfants ont soif d’apprendre. Ils savent que l’éducation est leur seule issue. Chaque année, de nombreux étudiants réussissent les examens nationaux contre toute attente. Ils rêvent de devenir médecins, ingénieurs et enseignants. Leurs familles sacrifient tout pour payer les petites sommes. Le gouvernement ne les aide pas. L’aide étrangère atteint rarement les salles de classe. Mais les gens n’abandonnent pas. Ils savent qu’un enfant avec un livre peut changer une famille. Ils savent qu’une nation qui lit peut se relever. Alors ils continuent à se battre, même quand le monde les oublie.",
        "caption": "Enfants apprenant dans une humble salle de classe – l’espoir vit encore"
    },
    {
        "title": "Leçon 9 : Le soutien de la famille et des amis",
        "image": lessons_en[8]["image"],
        "text": "Une chose qui maintient Haïti en vie, c’est la solidarité entre ses habitants. Quand une famille ne peut pas payer un enterrement, les voisins collectent de l’argent. Quand une mère tombe malade, sa sœur cuisine pour ses enfants. Quand un jeune homme veut créer une entreprise, ses amis lui prêtent ce qu’ils peuvent. Ce n’est pas de la charité. C’est ainsi que nous survivons. J’ai vu un frère donner sa dernière gourde pour que sa sœur puisse acheter des médicaments. J’ai vu des cousins partager une chambre pour qu’un jeune couple marié ait de l’intimité. Ceux qui vivent à l’étranger envoient de l’argent chaque mois. Ils appellent tous les dimanches pour avoir des nouvelles. Ils envisagent de revenir un jour, quand le pays sera sûr. Ce réseau d’amour est notre banque. C’est notre assurance. C’est notre espoir. Le monde ne voit pas ce système invisible. Il ne voit que les gangs, la pauvreté et la politique. Mais à l’intérieur des maisons, il y a des milliers de petits actes de gentillesse. Ces actes sont le véritable trésor d’Haïti. Ils ne peuvent être volés ni bombardés. Ce sont ceux que le monde a oublié de remarquer.",
        "caption": "Une réunion de famille – la solidarité maintient Haïti fort"
    },
    {
        "title": "Leçon 10 : La mort du président – un tournant",
        "image": lessons_en[9]["image"],
        "text": "La nuit du 7 juillet 2021, tout a changé. Le président Jovenel Moïse a été assassiné dans sa propre chambre. Tout le pays s’est réveillé dans un cauchemar. Personne ne savait qui l’avait fait ni pourquoi. Les forces de sécurité étaient désorientées. Les gangs ont profité du chaos. Ils se sont étendus à de nouveaux quartiers. Les enlèvements, les meurtres et les pillages ont augmenté chaque jour. L’économie, déjà fragile, s’est encore effondrée. Les investisseurs internationaux ont fui. Les touristes étaient déjà partis depuis longtemps. Maintenant, même les travailleurs humanitaires ont commencé à partir. Le gouvernement ne pouvait pas contrôler les rues. La police était en infériorité numérique et en infériorité d’armement. Les gens se sentaient abandonnés. Il n’y avait ni président, ni parlement, ni justice. Les gangs dirigeaient littéralement le pays. Ce jour a marqué la fin de tout espoir de redressement rapide. Le monde a condamné l’assassinat. Mais il n’a offert aucune aide réelle. Haïti a été laissé brûler tout seul. Et le feu ne s’est pas éteint depuis. La question demeure : qui a profité de ce chaos ? La réponse est encore inconnue. Mais un jour, la vérité éclatera. En attendant, le peuple paie le prix chaque jour.",
        "caption": "Un palais présidentiel obscurci – symbole d’une nation en crise"
    },
    {
        "title": "Leçon 11 : Vivre sous l’emprise de l’insécurité",
        "image": lessons_en[10]["image"],
        "text": "L’insécurité est devenue une réalité quotidienne pour chaque Haïtien. Je ne peux pas aller au marché sans craindre d’être kidnappé. Ma sœur ne peut pas prendre la voiture pour aller travailler car les gangs ont bloqué la route. Les enfants ne peuvent pas jouer dehors après midi. Le bruit des coups de feu est plus courant que le bruit des rires. Nous avons appris à identifier quel gang contrôle quelle rue. Nous leur payons des taxes, ou nous risquons notre vie. Certaines personnes ont cessé d’aller à l’église. Les mariages et les enterrements sont petits, rapides et silencieux. Les écoles ferment tôt pour que les enfants rentrent avant la nuit. Nous communiquons par WhatsApp pour savoir quelles routes sont sûres. Chaque jour apporte une nouvelle histoire d’horreur. Un voisin enlevé de sa voiture. Une jeune fille tuée parce que son père a refusé de payer une rançon. Un chauffeur brûlé vif dans son bus. La police ne vient pas. L’armée n’existe pas. Nous sommes seuls avec les hommes armés. Le monde connaît notre insécurité, mais il ne fait rien. Ils envoient des notes diplomatiques et des condamnations. Ils n’envoient pas de soldats ni d’aide réelle. Alors les gangs deviennent plus forts, et nous devenons plus faibles. Et le monde continue de défiler devant notre souffrance.",
        "caption": "Hommes armés dans une rue – la réalité quotidienne de l’insécurité"
    },
    {
        "title": "Leçon 12 : L’impôt inflationniste",
        "image": lessons_en[11]["image"],
        "text": "L’inflation est un voleur silencieux qui nous dépouille chaque jour. Quand la gourde perd de la valeur, nos économies disparaissent. Ceux qui ont travaillé trente ans ne peuvent pas prendre leur retraite. Leur pension ne vaut rien. Les jeunes ne peuvent pas économiser pour une maison ou un mariage. Ils dépensent tout ce qu’ils gagnent en nourriture de base. Le prix du riz, de l’huile et du sucre importés augmente chaque semaine. Les produits locaux deviennent aussi plus chers, car les agriculteurs ne peuvent pas se permettre le carburant. Le boulanger ne peut pas acheter de farine, donc le pain devient un luxe. Le cuisinier ne peut pas acheter de charbon de bois, donc les repas chauds sont rares. La mère ne peut pas acheter de lait, donc les bébés boivent une bouillie coupée d’eau. Chaque fois que nous allons à la banque, le taux de change est pire. Les gens avec des dollars sont des rois. Les gens avec des gourdes sont des mendiants. La banque centrale essaie de contrôler l’inflation, mais c’est comme retenir l’océan. La vraie cause est l’instabilité politique et la fuite des capitaux. Les riches envoient leur argent à l’étranger. Les pauvres sont laissés avec du papier sans valeur. Ce n’est pas une crise économique. C’est une exécution lente. Le monde envoie de la nourriture parfois, mais il n’envoie pas la justice. Alors nous payons l’impôt inflationniste chaque jour, et personne ne nous aide.",
        "caption": "Une pile de monnaie locale – perdant de la valeur chaque jour"
    },
    {
        "title": "Leçon 13 : Malgré tout, nous rions",
        "image": lessons_en[12]["image"],
        "text": "Même dans la pire des crises, les Haïtiens n’ont pas oublié comment rire. Je regarde mes voisins s’asseoir sur leurs marches avant le soir et raconter des blagues. Ils se moquent des politiciens et des gangs. Ils rient de leurs propres poches vides. Le rire est une sorte de médecine. Il nous rappelle que nous sommes toujours en vie. Le dimanche, certaines personnes s’habillent encore et vont à l’église. Ils chantent fort, comme s’ils n’avaient pas peur. Les jeunes jouent au football dans les terrains vides, même s’ils n’ont pas de chaussures. Les mères tressent encore les cheveux de leurs filles avec des rubans colorés. Les pères jouent encore aux dominos avec leurs amis. La radio joue encore du kompa, et parfois nous dansons dans le salon. Nous ne pouvons pas laisser les gangs voler notre joie. Ce serait une seconde mort. Alors nous choisissons de célébrer les petites choses. Un bon repas. Une nuit sûre. Un enfant qui a réussi un examen. Un ami revenu de l’étranger. Ces moments sont notre trésor. Le monde ne voit pas nos rires. Il ne voit que les gros titres. Mais nos rires sont plus forts que les armes. Et c’est ainsi que nous survivons.",
        "caption": "Enfants jouant dans la rue – la joie existe encore"
    },
    {
        "title": "Leçon 14 : L’aide de la diaspora",
        "image": lessons_en[13]["image"],
        "text": "Chaque mois, des millions de dollars sont envoyés par les Haïtiens vivant à l’étranger. Ils travaillent dans des usines en République dominicaine. Ils conduisent des taxis à New York et à Miami. Ils nettoient des hôpitaux à Paris et à Montréal. Ils sont partis parce qu’ils ne trouvaient pas de travail ici. Mais ils n’ont jamais oublié leurs familles. L’argent qu’ils envoie sert à payer les frais de scolarité, les factures médicales et les enterrements. Il achète du riz, de l’huile et des médicaments. Il répare les toits et achète des poulets. Sans cette aide, la moitié du pays mourrait de faim. La diaspora est notre bouée de sauvetage. Ils envoient aussi des vêtements, des chaussures et des jouets. Ils paient les mariages et les baptêmes. Ils appellent chaque semaine pour entendre la voix de leurs parents. Certains ont économisé pendant des années pour construire une petite maison dans leur village. Ils rêvent de revenir quand le pays sera sûr. Ils sont la main invisible qui maintient Haïti debout. Le monde ne les remercie pas. Mais nous, oui. Chaque matin, nous nous réveillons grâce à eux. Chaque nuit, nous dormons grâce à eux. La diaspora est le vrai héros de cette histoire. Et elle ne laissera pas Haïti mourir.",
        "caption": "Un guichet de transfert d’argent – symbole du soutien de la diaspora"
    },
    {
        "title": "Leçon 15 : Une lueur de calme",
        "image": lessons_en[14]["image"],
        "text": "Fin 2025, quelque chose d’inattendu s’est produit. La violence a commencé à diminuer. Certains gangs ont quitté leurs bastions. D’autres se sont déplacés vers la campagne. Les routes principales sont devenues plus sûres. Les gens ont recommencé à sortir pour acheter de la nourriture. Les enfants sont retournés à l’école sans peur. Les marchés se sont remplis de vendeurs. La police a réussi à arrêter quelques chefs de gangs. Les pressions internationales ont forcé certains pays à cesser de vendre des armes aux gangs. Les Nations Unies ont envoyé une petite mission de soutien. Ce n’était pas parfait, mais cela a aidé. Le calme n’est pas venu par hasard. Beaucoup pensent qu’il a été orchestré. Quelqu’un a planifié la fin du chaos à un moment précis. Qui a bénéficié de la paix ? Les mêmes personnes qui ont bénéficié de la guerre ? La réponse n’est pas encore connue. Le procès des accusés du meurtre du président va bientôt commencer. Beaucoup espèrent que la vérité éclatera. Pour l’instant, nous respirons un peu plus facilement. Il y a une lueur d’espoir. Mais nous avons déjà été déçus. Alors nous attendons et regardons. Le monde peut encore nous oublier. Mais nous, nous nous souviendrons de tout.",
        "caption": "Une rue calme à Port‑au‑Prince – signe d’un calme fragile"
    },
    {
        "title": "Leçon 16 : La recherche de la justice",
        "image": lessons_en[15]["image"],
        "text": "La justice est un mot que les Haïtiens ont entendu toute leur vie mais rarement vu. Le procès de ceux qui sont accusés d’avoir tué le président Moïse est un test. Les puissants seront-ils tenus responsables ? Ou achèteront-ils leur liberté ? Les gens regardent les tribunaux avec des yeux fatigués. Ils ont vu trop d’affaires reportées. Trop de juges corrompus. Trop de témoins tués. Mais cette fois, c’est différent. Il y a une pression internationale. Il y a des journalistes qui regardent. Les familles des victimes exigent la vérité. Les jeunes dans les rues scandent pour la justice. Ils savent que sans elle, le cycle se répétera. Un autre président sera tué. Une autre crise commencera. Une autre génération souffrira. Alors ils marchent, ils écrivent, ils prient. Ils envoient des courriels aux ambassades étrangères. Ils postent sur les réseaux sociaux. Ils ne laisseront pas la vérité être enterrée. Le procès aura lieu, et le monde y prête enfin attention. C’est un petit pas, mais c’est un pas. Si la justice vient, Haïti pourra enfin guérir. Si elle ne vient pas, le peuple saura que le monde l’a vraiment abandonné. Mais ils continueront à se battre. Parce que se battre pour la justice est la seule façon de vivre.",
        "caption": "Une salle d’audience – l’espoir de la justice"
    },
    {
        "title": "Leçon 17 : Comment en sommes-nous arrivés là ?",
        "image": lessons_en[16]["image"],
        "text": "Comment Haïti est‑il passé de la Perle des Caraïbes à une nation oubliée ? Certains disent que tout a commencé avec la dette d’indépendance. D’autres pointent les dictatures Duvalier. Certains accusent la communauté internationale pour des décennies d’ingérence. D’autres disent que c’est la faute de mauvais dirigeants. La vérité est que de nombreuses forces ont agi ensemble. Les puissances étrangères ont affamé l’économie haïtienne. Les dirigeants locaux ont volé l’argent de la nation. Les catastrophes naturelles ont brisé ses infrastructures. Les gangs ont détruit sa sécurité. Le monde a détourné le regard parce qu’Haïti n’avait ni pétrole ni or à offrir. Il n’y avait aucun profit à aider. Alors le pays est tombé. Pierre après pierre, le mur s’est effondré. Le peuple n’a pas pu l’arrêter. Ils étaient trop pauvres, trop faibles, trop divisés. Nous restons maintenant avec les décombres. La question est : pouvons‑nous reconstruire ? La réponse dépend de si le monde nous verra enfin. Pas comme un cas de charité, mais comme une nation de gens fiers. Pas comme un problème à gérer, mais comme un partenaire à respecter. Nous ne sommes pas arrivés ici par accident. Nous sommes arrivés ici à cause des choix des puissants. Ces choix ne sont pas irréversibles. Mais ils ne seront pas inversés à moins que le monde ne se souvienne. Et jusqu’à présent, le monde a oublié.",
        "caption": "Une carte d’Haïti – demandant pourquoi la perle a été perdue"
    },
    {
        "title": "Leçon 18 : Le rôle des médias",
        "image": lessons_en[17]["image"],
        "text": "Les médias internationaux ont joué un grand rôle dans l’histoire oubliée d’Haïti. Quand une catastrophe frappe, les caméras arrivent. Elles montrent les cadavres et les décombres. Elles interviewent les enfants affamés et les mères en pleurs. Puis, quand le cycle de l’information se termine, les caméras repartent. Elles ne restent pas pour montrer la reconstruction. Elles ne font pas de reportages sur les petites victoires. Elles ne racontent pas les histoires des enseignants qui travaillent sans salaire. Elles ne mentionnent pas les artistes qui peignent dans le noir. Les médias vendent la tragédie, pas l’espoir. Et ainsi le monde ne voit Haïti que comme un lieu de tristesse. Les gens s’engourdissent devant les images. Ils cessent de donner. Ils cessent de s’inquiéter. Haïti devient un bruit de fond. Voilà comment un pays est oublié. Non par le silence, mais par une narration sélective. Les Haïtiens ne veulent pas de pitié. Ils veulent la solidarité. Ils veulent que le monde voie leur force, pas seulement leur souffrance. Mais les médias ne diffusent pas la force. Alors le monde reste ignorant. Si vous voulez vous souvenir d’Haïti, vous devez regarder au‑delà des titres. Vous devez écouter les histoires qui ne sont pas racontées. C’est ce que ce livre essaie de faire.",
        "caption": "Une caméra de journal – comment le monde voit Haïti"
    },
    {
        "title": "Leçon 19 : Que peut‑on faire ?",
        "image": lessons_en[18]["image"],
        "text": "La situation en Haïti est désespérée, mais elle n’est pas sans espoir. Voici des mesures qui peuvent tout changer. Premièrement, la communauté internationale doit soutenir une véritable mission de sécurité. Non pas avec des mots, mais avec des soldats et de l’argent. Deuxièmement, le gouvernement haïtien doit être restructuré. La corruption doit être punie, non récompensée. Troisièmement, l’investissement étranger doit être encouragé dans des zones sûres. Des emplois calmeront la colère des jeunes. Quatrièmement, l’éducation doit être financée. Une population alphabétisée peut construire une nation stable. Cinquièmement, l’agriculture doit être modernisée. Haïti peut se nourrir sans riz étranger. Sixièmement, la diaspora doit être invitée à revenir avec ses compétences. Septièmement, le procès pour le meurtre du président doit être juste et transparent. Huitièmement, la gouvernance locale doit être renforcée. Neuvièmement, les gangs doivent être désarmés par une force sérieuse. Dixièmement, le monde doit changer sa vision d’Haïti. Non pas comme un problème, mais comme un partenaire. Ces mesures ne sont pas impossibles. D’autres pays sont sortis de situations pires. Mais il faudra de la volonté. Il faudra du courage. Et il faudra que le monde se souvienne qu’Haïti existe encore. Nous ne pouvons pas le faire seuls. Nous avons besoin d’amis qui ne fuient pas au premier signe de difficulté. Nous avons besoin d’amis qui restent. Êtes‑vous l’un d’eux ? L’avenir n’est pas encore écrit. Aidez‑nous à écrire un nouveau chapitre.",
        "caption": "Des mains construisant une maison – la reconstruction est possible"
    },
    {
        "title": "Leçon 20 : La Perle peut briller à nouveau",
        "image": lessons_en[19]["image"],
        "text": "La Perle des Caraïbes a été recouverte de poussière, mais elle n’est pas détruite. Sous les décombres, il y a encore de la beauté. Sous la peur, il y a encore du courage. Sous la faim, il y a encore de la dignité. Haïti s’est déjà relevé, et il peut se relever encore. Les jeunes que je vois chaque jour me donnent de l’espoir. Ils apprennent le codage sur de vieux ordinateurs portables. Ils pratiquent l’anglais en regardant YouTube. Ils créent de petites entreprises avec presque rien. Ils organisent des patrouilles de quartier pour éloigner les gangs. Ils n’attendent pas que le monde les sauve. Ils se sauvent eux‑mêmes. Mais ils ont besoin d’aide. Un coup de main, pas une aumône. Un investissement, pas la pitié. Une chance, pas une charité. Si vous lisez ceci, vous avez le pouvoir de faire partie de la solution. Vous pouvez donner directement à des organisations haïtiennes. Vous pouvez faire pression sur votre gouvernement pour qu’il soutienne une véritable mission de sécurité. Vous pouvez visiter Haïti quand ce sera sûr, et dire au monde ce que vous voyez. Vous pouvez partager les véritables histoires d’Haïti, pas seulement les tragédies. La perle est toujours là. Elle attend la lumière. Allez‑vous nous aider à la polir ? L’histoire d’Haïti n’est pas finie. Le prochain chapitre s’écrit en ce moment même. Faisons en sorte que ce soit une histoire d’espoir, de justice et de renaissance. Le monde a oublié Haïti. Mais Haïti ne s’est jamais oubliée. Et nous ne vous laisserons pas nous oublier à nouveau.",
        "caption": "Un jeune artiste haïtien peignant – la perle brille encore de l’intérieur"
    }
]

# ---------- SPANISH TRANSLATIONS ----------
lessons_es = [
    {
        "title": "Lección 1: La Perla del Caribe",
        "image": lessons_en[0]["image"],
        "text": "Érase una vez, Haití era llamada la Perla del Caribe. Su sol era cálido y acogedor. Llegaban turistas de todo el mundo para disfrutar de las playas doradas. Visitaban los viejos museos de Puerto Príncipe. Se alojaban en hermosos hoteles enclavados en el campo. La gente recibía a los visitantes con el corazón abierto. La música y las risas llenaban las calles cada atardecer. Los agricultores vendían mangos frescos y café junto a las carreteras. Los artesanos tallaban esculturas de madera que asombraban a todos. La Ciudadela se alzaba orgullosa en la cima de la montaña, símbolo de libertad. Haití fue la primera república negra en abolir la esclavitud. Su historia inspiró al mundo. Pero con los años, las tormentas políticas comenzaron a acumularse. La perla empezó a perder su brillo. Y lentamente, el mundo comenzó a olvidar.",
        "caption": "Una hermosa playa haitiana al atardecer"
    },
    {
        "title": "Lección 2: Una tierra de rica historia",
        "image": lessons_en[1]["image"],
        "text": "La historia de Haití es diferente a cualquier otra. Los taínos vivieron allí primero, llamándola Ayiti, tierra de altas montañas. Luego vinieron los franceses, que trajeron esclavos de África. Los esclavos se levantaron en una gran rebelión liderada por Toussaint Louverture. Lucharon durante doce largos años. En 1804, Haití se convirtió en la primera república negra libre del mundo. La victoria causó conmoción en toda América. Otras naciones temían que sus propios esclavos se rebelaran. Así que aislaron a Haití, negándose a reconocer su independencia. Exigieron un enorme pago como compensación. Durante décadas, Haití pagó a Francia por su libertad. Esa deuda paralizó a la joven nación. Aún hoy, esa injusticia original sigue resonando. Los turistas una vez se maravillaron con el Palacio Sans‑Souci. Recorrían las ruinas de la Ciudadela. Pero esas maravillas ahora son visitadas solo por unos pocos. El mundo olvidó porque eligió mirar hacia otro lado.",
        "caption": "La Ciudadela Laferrière – un símbolo de la libertad haitiana"
    },
    {
        "title": "Lección 3: El sol, el mar y las sonrisas",
        "image": lessons_en[2]["image"],
        "text": "Recuerdo cuando era niño, mi familia me llevaba a las playas de Jacmel. El agua era tan clara que se podían ver todos los peces. Mi madre preparaba plátanos fritos y naranjas frescas. Mi padre contaba historias de antaño. Otras familias también estaban allí, riendo y chapoteando. Todos se sentían seguros. El sol siempre brillaba, y la brisa traía olor a sal. Había visitantes de Canadá, Francia y Estados Unidos. Bailaban música kompa en la arena. Compraban pinturas de artistas locales. Los dueños de los hoteles sonreían porque sus habitaciones estaban llenas. Los pescadores traían pescado para vender. Todos ganaban un sustento. Aquellos días no eran perfectos, pero eran felices. Ahora, cuando conduzco hacia la misma playa, veo hoteles vacíos. La arena sigue ahí, pero los turistas se han ido. Las sonrisas son más difíciles de encontrar. El mundo olvidó lo que teníamos para ofrecer.",
        "caption": "Una playa haitiana tranquila – todavía hermosa, pero vacía de visitantes"
    },
    {
        "title": "Lección 4: Las primeras grietas en la Perla",
        "image": lessons_en[3]["image"],
        "text": "Los problemas no comenzaron de la noche a la mañana. Comenzaron con pequeñas grietas en los cimientos. Después del gran terremoto de 2010, Haití recibió miles de millones de dólares en ayuda. Solo una fracción llegó a las personas que la necesitaban. Organizaciones extranjeras hicieron promesas vacías. Se planearon nuevas carreteras pero nunca se construyeron. Se prometieron escuelas pero quedaron en escombros. El gobierno era débil y a menudo corrupto. La gente se cansó de esperar. Las pandillas comenzaron a tomar el control de los vecindarios. Ofrecían seguridad y comida donde el Estado no podía. Con el tiempo, esas pandillas se hicieron más fuertes. Los secuestros por rescate se volvieron comunes. Los negocios cerraron y los empleos desaparecieron. La clase media comenzó a irse. Los ricos construyeron muros altos alrededor de sus casas. Los pobres no tenían a dónde ir. Las grietas se ensancharon. El mundo observó sin hacer nada. Cuando alguien finalmente se dio cuenta, la perla ya se había hecho pedazos.",
        "caption": "Escombros después del terremoto de 2010 – un punto de inflexión"
    },
    {
        "title": "Lección 5: Cuando los turistas dejaron de venir",
        "image": lessons_en[4]["image"],
        "text": "Trabajaba como guía en un pequeño hotel en Cabo Haitiano. Cada mañana, recibía a los huéspedes con una sonrisa. Venían de cruceros que atracaban en el puerto. Les mostraba la Ciudadela y el Palacio del Rey. Les encantaba la historia y las vistas. El hotel tenía cincuenta habitaciones, y la mayoría de las noches estaban llenas. Ganaba lo suficiente para ayudar a mi madre y a mi hermano menor. Entonces la situación de seguridad comenzó a cambiar. Los gobiernos extranjeros emitieron advertencias de viaje. Los cruceros dejaron de venir. El hotel cerró sus puertas. Perdí mi trabajo, como cientos de otros. El restaurante de al lado también cerró. El mercado de recuerdos se vació. Los conductores que llevaban a los turistas se quedaron sin trabajo. Todos vimos cómo los barcos se alejaban hacia otras islas. República Dominicana, Jamaica y Puerto Rico les dieron la bienvenida. Haití fue dejado atrás. El mundo no dejó de viajar. Simplemente viajó a otro lugar. Y Haití fue olvidado.",
        "caption": "Piscina de hotel vacía – un signo de turismo perdido"
    },
    {
        "title": "Lección 6: El dolor de la inflación",
        "image": lessons_en[5]["image"],
        "text": "La inflación es una palabra que muchos haitianos conocen ahora demasiado bien. Hace cinco años, una bolsa de arroz costaba 250 gourdes. Hoy, esa misma bolsa cuesta 1.200 gourdes. Una pequeña botella de aceite de cocina se ha triplicado de precio. El mercado está lleno de comida, pero nadie puede pagarla. Veo a madres contando monedas para comprar unos pocos tomates. Los padres saltan comidas para que sus hijos puedan comer. El salario que una vez alimentó a una familia durante una semana ahora dura solo dos días. La gente ha dejado de comprar carne o huevos. Solo comen arroz y frijoles, a veces ni eso. La moneda local ha perdido su valor frente al dólar. Quienes reciben dinero del extranjero pueden sobrevivir. Quienes dependen del trabajo local luchan. Observo a mis vecinos vender muebles, luego ropa, luego esperanza. La inflación es como un fuego lento. No te quema todo de una vez. Pero un día te despiertas y todo lo que tenías se ha ido. El mundo no siente este fuego, por lo tanto, al mundo no le importa.",
        "caption": "Un puesto de mercado con mercancías demasiado caras"
    },
    {
        "title": "Lección 7: El hambre que nunca se va",
        "image": lessons_en[6]["image"],
        "text": "El hambre se ha convertido en un visitante permanente en muchos hogares. Recuerdo cuando mi abuela cocinaba una gran olla de sopa joumou cada domingo. Toda la familia se reunía para comer y reír. Ahora, la sopa joumou es un lujo para los ricos. Los niños van a la escuela con el estómago vacío. Se desmayan en clase porque no han comido. Los maestros usan su propio dinero para comprar bocadillos. El Programa Mundial de Alimentos ha reducido su ayuda. La producción local de alimentos ha caído porque los agricultores no pueden comprar semillas. Las pandillas controlan las carreteras, por lo que los alimentos no pueden llegar a las ciudades. En el campo, la gente come raíces y hojas silvestres. En Puerto Príncipe, las familias comparten una comida al día. He visto bebés demasiado débiles para llorar. El hambre no es causada por una sequía o una inundación. Es causada por el colapso de todo un sistema. El mundo envía dinero ocasionalmente, pero no envía justicia. Y sin justicia, los hambrientos no pueden ser alimentados.",
        "caption": "Un niño comiendo un simple plato de arroz – el hambre está en todas partes"
    },
    {
        "title": "Lección 8: La educación contra todo pronóstico",
        "image": lessons_en[7]["image"],
        "text": "Incluso en los momentos más oscuros, los padres haitianos luchan por la educación de sus hijos. Conozco a una madre que camina dos horas cada día para vender carbón vegetal. Lo hace para que su hijo pueda permanecer en la escuela. Su uniforme está remendado, pero está limpio. Sus libros son prestados, pero los lee todas las noches. La escuela no tiene ventanas y a veces no tiene techo. La maestra recibe muy poco pago, pero aún así viene. No hay computadoras ni proyectores. Aprenden escribiendo en pequeñas pizarras. Pero los niños están ansiosos por aprender. Saben que la educación es su única salida. Cada año, muchos estudiantes aprueban los exámenes nacionales contra todo pronóstico. Sueñan con convertirse en médicos, ingenieros y maestros. Sus familias lo sacrifican todo para pagar las pequeñas tarifas. El gobierno no los ayuda. La ayuda extranjera rara vez llega a las aulas. Pero la gente no se rinde. Saben que un niño con un libro puede cambiar una familia. Saben que una nación que lee puede levantarse. Así que siguen luchando, incluso cuando el mundo los olvida.",
        "caption": "Niños aprendiendo en una humilde aula – la esperanza aún vive"
    },
    {
        "title": "Lección 9: El apoyo de la familia y los amigos",
        "image": lessons_en[8]["image"],
        "text": "Una cosa que mantiene viva a Haití es la solidaridad entre su gente. Cuando una familia no puede pagar un funeral, los vecinos recolectan dinero. Cuando una madre se enferma, su hermana cocina para sus hijos. Cuando un joven quiere iniciar un negocio, sus amigos le prestan lo que pueden. Esto no es caridad. Así es como sobrevivimos. He visto a un hermano dar su último gourde para que su hermana pueda comprar medicina. He visto a primos compartir una habitación para que una pareja recién casada tenga privacidad. Quienes viven en el extranjero envían dinero a casa cada mes. Llaman todos los domingos para escuchar las noticias. Planean regresar algún día, cuando el país esté seguro. Esta red de amor es nuestro banco. Es nuestro seguro. Es nuestra esperanza. El mundo no ve este sistema invisible. Solo ve las pandillas, la pobreza y la política. Pero dentro de los hogares, hay miles de pequeños actos de bondad. Esos actos son el verdadero tesoro de Haití. No pueden ser robados ni bombardeados. Son lo que el mundo olvidó notar.",
        "caption": "Una reunión familiar – la solidaridad mantiene fuerte a Haití"
    },
    {
        "title": "Lección 10: La muerte del presidente – un punto de inflexión",
        "image": lessons_en[9]["image"],
        "text": "La noche del 7 de julio de 2021, todo cambió. El presidente Jovenel Moïse fue asesinado en su propia habitación. Todo el país despertó en una pesadilla. Nadie sabía quién lo había hecho ni por qué. Las fuerzas de seguridad estaban confundidas. Las pandillas aprovecharon el caos. Se expandieron a nuevos vecindarios. Los secuestros, asesinatos y saqueos aumentaron cada día. La economía, ya débil, colapsó aún más. Los inversores internacionales huyeron. Los turistas ya se habían ido mucho antes. Ahora incluso los trabajadores humanitarios comenzaron a irse. El gobierno no podía controlar las calles. La policía estaba superada en número y en armamento. La gente se sintió abandonada. No había presidente, no había parlamento, no había justicia. Las pandillas literalmente gobernaban el país. Ese día marcó el fin de cualquier esperanza de una rápida recuperación. El mundo condenó el asesinato. Pero no ofreció ninguna ayuda real. Haití fue dejado arder por sí solo. Y el fuego no se ha apagado desde entonces. La pregunta sigue siendo: ¿quién se benefició de este caos? La respuesta aún se desconoce. Pero algún día saldrá la verdad. Hasta entonces, el pueblo paga el precio cada día.",
        "caption": "Un palacio presidencial oscurecido – símbolo de una nación en crisis"
    },
    {
        "title": "Lección 11: Viviendo bajo el control de la inseguridad",
        "image": lessons_en[10]["image"],
        "text": "La inseguridad se ha convertido en una realidad diaria para cada haitiano. No puedo ir al mercado sin miedo a ser secuestrado. Mi hermana no puede conducir al trabajo porque las pandillas han bloqueado la carretera. Los niños no pueden jugar afuera después del mediodía. El sonido de los disparos es más común que el sonido de las risas. Hemos aprendido a identificar qué pandilla controla qué calle. Les pagamos impuestos o arriesgamos nuestras vidas. Algunas personas han dejado de ir a la iglesia. Las bodas y los funerales son pequeños, rápidos y silenciosos. Las escuelas cierran temprano para que los niños lleguen a casa antes del anochecer. Nos comunicamos por WhatsApp para saber qué carreteras son seguras. Cada día trae una nueva historia de horror. Un vecino sacado de su coche. Una joven asesinada porque su padre se negó a pagar un rescate. Un conductor quemado vivo en su autobús. La policía no viene. El ejército no existe. Estamos solos con los hombres armados. El mundo sabe de nuestra inseguridad, pero no hace nada. Envían notas diplomáticas y condenas. No envían soldados ni ayuda real. Así que las pandillas se vuelven más fuertes, y nosotros más débiles. Y el mundo sigue deslizando el dedo sobre nuestro sufrimiento.",
        "caption": "Hombres armados en una calle – la realidad diaria de la inseguridad"
    },
    {
        "title": "Lección 12: El impuesto inflacionario",
        "image": lessons_en[11]["image"],
        "text": "La inflación es un ladrón silencioso que nos roba cada día. Cuando el gourde pierde valor, nuestros ahorros desaparecen. Quienes trabajaron durante treinta años no pueden jubilarse. Su pensión no vale nada. Los jóvenes no pueden ahorrar para una casa o una boda. Gastan todo lo que ganan en alimentos básicos. El precio del arroz, el aceite y el azúcar importados sube cada semana. Los productos locales también se vuelven más caros porque los agricultores no pueden pagar el combustible. El panadero no puede comprar harina, por lo que el pan se convierte en un lujo. El cocinero no puede comprar carbón vegetal, por lo que las comidas calientes son escasas. La madre no puede comprar leche, por lo que los bebés beben gachas aguadas. Cada vez que vamos al banco, el tipo de cambio es peor. Las personas con dólares son reyes. Las personas con gourdes son mendigos. El banco central intenta controlar la inflación, pero es como contener el océano. La causa real es la inestabilidad política y la fuga de capitales. Los ricos envían su dinero al extranjero. Los pobres se quedan con papel sin valor. Esto no es una crisis económica. Es una ejecución lenta. El mundo envía comida a veces, pero no envía justicia. Así que pagamos el impuesto inflacionario cada día, y nadie nos ayuda.",
        "caption": "Una pila de moneda local – perdiendo valor cada día"
    },
    {
        "title": "Lección 13: A pesar de todo, reímos",
        "image": lessons_en[12]["image"],
        "text": "Incluso en la peor crisis, los haitianos no han olvidado cómo reír. Observo a mis vecinos sentarse en sus escalones frontales por la noche y contar chistes. Se burlan de los políticos y de las pandillas. Se ríen de sus propios bolsillos vacíos. La risa es una especie de medicina. Nos recuerda que todavía estamos vivos. Los domingos, algunas personas todavía se visten y van a la iglesia. Cantan fuerte, como si no tuvieran miedo. Los jóvenes juegan al fútbol en los terrenos vacíos, incluso si no tienen zapatos. Las madres todavía trenzan el cabello de sus hijas con cintas de colores. Los padres todavía juegan al dominó con sus amigos. La radio todavía toca kompa, y a veces bailamos en la sala. No podemos dejar que las pandillas roben nuestra alegría. Eso sería una segunda muerte. Así que elegimos celebrar las cosas pequeñas. Una buena comida. Una noche segura. Un niño que aprobó un examen. Un amigo que regresó del extranjero. Estos momentos son nuestro tesoro. El mundo no ve nuestra risa. Solo ve los titulares. Pero nuestra risa es más fuerte que las armas. Y así es como sobrevivimos.",
        "caption": "Niños jugando en la calle – la alegría todavía existe"
    },
    {
        "title": "Lección 14: La ayuda de la diáspora",
        "image": lessons_en[13]["image"],
        "text": "Cada mes, los haitianos que viven en el extranjero envían a casa millones de dólares. Trabajan en fábricas en la República Dominicana. Conducen taxis en Nueva York y Miami. Limpian hospitales en París y Montreal. Se fueron porque no pudieron encontrar trabajo aquí. Pero nunca olvidaron a sus familias. El dinero que envían paga la matrícula escolar, las facturas médicas y los funerales. Compra arroz, aceite y medicinas. Repara techos y compra pollos. Sin esta ayuda, la mitad del país pasaría hambre. La diáspora es nuestro salvavidas. También envían ropa, zapatos y juguetes. Pagan bodas y bautizos. Llaman todas las semanas para escuchar las voces de sus padres. Algunos han ahorrado durante años para construir una pequeña casa en su aldea. Sueñan con regresar cuando el país esté seguro. Son la mano invisible que mantiene a Haití en pie. El mundo no les da las gracias. Pero nosotros sí. Cada mañana, nos despertamos gracias a ellos. Cada noche, dormimos gracias a ellos. La diáspora es el verdadero héroe de esta historia. Y no dejará que Haití muera.",
        "caption": "Una tienda de transferencia de dinero – símbolo del apoyo de la diáspora"
    },
    {
        "title": "Lección 15: Un destello de calma",
        "image": lessons_en[14]["image"],
        "text": "A finales de 2025, ocurrió algo inesperado. La violencia comenzó a disminuir. Algunas pandillas abandonaron sus bastiones. Otras se trasladaron al campo. Las carreteras principales se volvieron más seguras. La gente empezó a salir de nuevo para comprar comida. Los niños regresaron a la escuela sin miedo. Los mercados se llenaron de vendedores. La policía logró arrestar a algunos líderes de pandillas. La presión internacional obligó a algunos países a dejar de vender armas a las pandillas. Las Naciones Unidas enviaron una pequeña misión de apoyo. No era perfecto, pero ayudó. La calma no llegó por accidente. Muchos creen que fue diseñada. Alguien planeó que el caos terminara en un momento determinado. ¿Quién se benefició de la paz? ¿Las mismas personas que se beneficiaron de la guerra? La respuesta aún no se conoce. El juicio de los acusados del asesinato del presidente comenzará pronto. Muchos esperan que salga la verdad. Por ahora, respiramos un poco más fácil. Hay un destello de esperanza. Pero ya hemos sido decepcionados antes. Así que esperamos y observamos. El mundo todavía puede olvidarnos. Pero nosotros lo recordaremos todo.",
        "caption": "Una calle tranquila en Puerto Príncipe – signo de una calma frágil"
    },
    {
        "title": "Lección 16: La búsqueda de la justicia",
        "image": lessons_en[15]["image"],
        "text": "La justicia es una palabra que los haitianos han oído toda su vida pero rara vez han visto. El juicio de los acusados de matar al presidente Moïse es una prueba. ¿Los poderosos serán responsables? ¿O comprarán su libertad? La gente mira los tribunales con ojos cansados. Han visto demasiados casos pospuestos. Demasiados jueces sobornados. Demasiados testigos asesinados. Pero esta vez se siente diferente. Hay presión internacional. Hay periodistas observando. Las familias de las víctimas exigen la verdad. Los jóvenes en las calles claman por justicia. Saben que sin ella, el ciclo se repetirá. Otro presidente será asesinado. Otra crisis comenzará. Otra generación sufrirá. Así que marchan, escriben y rezan. Envían correos electrónicos a las embajadas extranjeras. Publican en las redes sociales. No dejarán que la verdad sea enterrada. El juicio se llevará a cabo, y el mundo finalmente está prestando atención. Es un pequeño paso, pero es un paso. Si la justicia llega, Haití finalmente podrá sanar. Si no, el pueblo sabrá que el mundo realmente lo ha abandonado. Pero ellos seguirán luchando. Porque luchar por la justicia es la única forma de vivir.",
        "caption": "Una sala de tribunal – la esperanza de justicia"
    },
    {
        "title": "Lección 17: ¿Cómo llegamos aquí?",
        "image": lessons_en[16]["image"],
        "text": "¿Cómo pasó Haití de ser la Perla del Caribe a una nación olvidada? Algunos dicen que comenzó con la deuda de independencia. Otros señalan las dictaduras de Duvalier. Algunos culpan a la comunidad internacional por décadas de injerencia. Otros dicen que es culpa de los malos líderes. La verdad es que muchas fuerzas actuaron juntas. Las potencias extranjeras hambrearon la economía haitiana. Los líderes locales robaron el dinero de la nación. Los desastres naturales destruyeron su infraestructura. Las pandillas destruyeron su seguridad. El mundo miró hacia otro lado porque Haití no tenía petróleo ni oro que ofrecer. No había beneficio en ayudar. Así que el país cayó. Piedra tras piedra, el muro se derrumbó. La gente no pudo detenerlo. Eran demasiado pobres, demasiado débiles, demasiado divididos. Ahora nos quedamos con los escombros. La pregunta es: ¿podemos reconstruir? La respuesta depende de si el mundo finalmente nos verá. No como un caso de caridad, sino como una nación de personas orgullosas. No como un problema a gestionar, sino como un socio a respetar. No llegamos aquí por accidente. Llegamos aquí por las decisiones de los poderosos. Esas decisiones no son irreversibles. Pero no se revertirán a menos que el mundo recuerde. Y hasta ahora, el mundo ha olvidado.",
        "caption": "Un mapa de Haití – preguntando por qué se perdió la perla"
    },
    {
        "title": "Lección 18: El papel de los medios",
        "image": lessons_en[17]["image"],
        "text": "Los medios internacionales han desempeñado un papel importante en la historia olvidada de Haití. Cuando ocurre un desastre, llegan las cámaras. Muestran los cadáveres y los escombros. Entrevistan a los niños hambrientos y a las madres que lloran. Luego, cuando termina el ciclo de noticias, las cámaras se van. No se quedan para mostrar la recuperación. No informan sobre las pequeñas victorias. No cuentan las historias de los maestros que trabajan sin paga. No mencionan a los artistas que pintan en la oscuridad. Los medios venden tragedia, no esperanza. Y así, el mundo ve a Haití solo como un lugar de tristeza. La gente se insensibiliza ante las imágenes. Dejan de donar. Dejan de preocuparse. Haití se convierte en un ruido de fondo. Así es como se olvida a un país. No por el silencio, sino por la narración selectiva. Los haitianos no quieren lástima. Quieren solidaridad. Quieren que el mundo vea su fuerza, no solo su sufrimiento. Pero los medios no transmiten la fuerza. Así que el mundo permanece ignorante. Si quieres recordar a Haití, debes mirar más allá de los titulares. Debes escuchar las historias que no se cuentan. Eso es lo que este libro intenta hacer.",
        "caption": "Una cámara de noticias – cómo el mundo ve a Haití"
    },
    {
        "title": "Lección 19: ¿Qué se puede hacer?",
        "image": lessons_en[18]["image"],
        "text": "La situación en Haití es desesperada, pero no es desesperanzadora. Hay pasos que pueden cambiar todo. Primero, la comunidad internacional debe apoyar una misión de seguridad real. No con palabras, sino con soldados y dinero. Segundo, el gobierno haitiano debe ser reestructurado. La corrupción debe ser castigada, no recompensada. Tercero, se debe fomentar la inversión extranjera en zonas seguras. Los empleos calmarán la ira de los jóvenes. Cuarto, se debe financiar la educación. Una población alfabetizada puede construir una nación estable. Quinto, se debe modernizar la agricultura. Haití puede alimentarse a sí mismo sin arroz extranjero. Sexto, se debe invitar a la diáspora a regresar con sus habilidades. Séptimo, el juicio por el asesinato del presidente debe ser justo y transparente. Octavo, se debe fortalecer la gobernanza local. Noveno, las pandillas deben ser desarmadas por una fuerza seria. Décimo, el mundo debe cambiar su visión de Haití. No como un problema, sino como un socio. Estos pasos no son imposibles. Otros países han surgido de situaciones peores. Pero se necesitará voluntad. Se necesitará coraje. Y se necesitará que el mundo recuerde que Haití todavía existe. No podemos hacerlo solos. Necesitamos amigos que no huyan ante el primer signo de problemas. Necesitamos amigos que se queden. ¿Eres uno de ellos? El futuro aún no está escrito. Ayúdanos a escribir un nuevo capítulo.",
        "caption": "Manos construyendo una casa – la reconstrucción es posible"
    },
    {
        "title": "Lección 20: La Perla puede brillar de nuevo",
        "image": lessons_en[19]["image"],
        "text": "La Perla del Caribe ha estado cubierta de tierra, pero no está destruida. Bajo los escombros, todavía hay belleza. Bajo el miedo, todavía hay coraje. Bajo el hambre, todavía hay dignidad. Haití ha resurgido antes, y puede resurgir de nuevo. Los jóvenes que veo cada día me dan esperanza. Aprenden programación en viejas computadoras portátiles. Practican inglés viendo YouTube. Empiezan pequeños negocios con casi nada. Organizan patrullas vecinales para mantener alejadas a las pandillas. No están esperando que el mundo los salve. Se están salvando a sí mismos. Pero necesitan ayuda. Una mano amiga, no una limosna. Inversión, no lástima. Una oportunidad, no una caridad. Si estás leyendo esto, tienes el poder de ser parte de la solución. Puedes donar directamente a organizaciones haitianas. Puedes presionar a tu gobierno para que apoye una misión de seguridad real. Puedes visitar Haití cuando sea seguro, y decirle al mundo lo que ves. Puedes compartir las verdaderas historias de Haití, no solo las tragedias. La perla sigue aquí. Está esperando la luz. ¿Nos ayudarás a pulirla? La historia de Haití no ha terminado. El próximo capítulo se está escribiendo ahora mismo. Asegurémonos de que sea una historia de esperanza, justicia y renacimiento. El mundo olvidó a Haití. Pero Haití nunca se ha olvidado a sí mismo. Y no dejaremos que nos olvides de nuevo.",
        "caption": "Un joven artista haitiano pintando – la perla aún brilla desde dentro"
    }
]

# ---------- MAP LANGUAGE TO LESSONS ----------
language_map = {
    "en": lessons_en,
    "fr": lessons_fr,
    "es": lessons_es
}

# ---------- LANGUAGE SELECTOR IN SIDEBAR ----------
lang_options = {
    "English": "en",
    "Français": "fr",
    "Español": "es"
}
selected_lang_name = st.sidebar.selectbox(
    _("language_selector"),
    list(lang_options.keys()),
    index=["en","fr","es"].index(st.session_state.lang)
)
st.session_state.lang = lang_options[selected_lang_name]
lessons = language_map[st.session_state.lang]

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
    st.markdown(f'<div class="sidebar-logo">{_("sidebar_logo")}</div>', unsafe_allow_html=True)
    st.markdown(f"## {_('sidebar_company')}")
    st.markdown(f"**{_('sidebar_founder')}**")
    st.markdown(_("sidebar_phone"))
    st.markdown(_("sidebar_email"))
    st.markdown("---")
    st.markdown(f"[{_('sidebar_website')}](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown(f"### {_('sidebar_book_title')}")
    st.markdown(_("sidebar_book_desc"))
    st.markdown("---")
    st.caption(_("sidebar_caption"))

# ---------- MAIN PAGE ----------
def main():
    st.markdown(
        f'<div class="main-header"><h1>{_("app_title")}</h1><p>{_("app_sub")}</p></div>',
        unsafe_allow_html=True
    )
    
    # Lesson selector in sidebar
    lesson_titles = [f"{i+1}. {lesson['title']}" for i, lesson in enumerate(lessons)]
    selected_idx = st.sidebar.selectbox(_("lesson_selector"), range(len(lessons)), format_func=lambda i: lesson_titles[i])
    
    lesson = lessons[selected_idx]
    
    # Display the lesson card
    with st.container():
        st.markdown(f'<div class="lesson-card">', unsafe_allow_html=True)
        col_img, col_text = st.columns([1, 2])
        with col_img:
            st.image(lesson['image'], caption=lesson.get('caption', 'Illustration'), use_container_width=True)
        with col_text:
            st.markdown(f"## {lesson['title']}")
            st.markdown(f'<div class="story-text">{lesson["text"]}</div>', unsafe_allow_html=True)
            
            # Read Aloud button
            read_btn = st.button(f"{_('read_aloud_button')} ({selected_idx+1})", key=f"read_{selected_idx}")
            if read_btn:
                indicator = st.empty()
                indicator.markdown(
                    f'<div class="reading-indicator"><span class="pulse-dot"></span> {_("reading_indicator")}</div>',
                    unsafe_allow_html=True
                )
                text_to_speak = lesson["text"].replace('"', '\\"').replace("\n", " ").replace("'", "\\'")
                js_code = f"""
                <script>
                    var utterance = new SpeechSynthesisUtterance("{text_to_speak}");
                    utterance.lang = {"'fr-FR'" if st.session_state.lang == "fr" else "'es-ES'" if st.session_state.lang == "es" else "'en-US'"};
                    utterance.onend = function() {{
                        var event = new CustomEvent('streamlit:setComponentValue', {{detail: {{value: "done"}}}});
                        window.dispatchEvent(event);
                    }};
                    window.speechSynthesis.cancel();
                    window.speechSynthesis.speak(utterance);
                </script>
                """
                components.html(js_code, height=0)
                st.success(_("reading_success"))
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown(f"""
    <div class="footer">
        <p>© {datetime.now().year} {_('footer_copyright')}</p>
        <p>{_('footer_book')}<br>{_('footer_built')}</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- PAGE ROUTING ----------
if __name__ == "__main__":
    main()
