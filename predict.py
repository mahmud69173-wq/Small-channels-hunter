from cog import BasePredictor, Input

class Predictor(BasePredictor):
    def setup(self):
        pass

    def predict(
        self,
        seed_hashtags: str = Input(description="Paste hashtags from videos separated by commas", default="#study tips,#AI tools,#productivity,#college success"),
        niche: str = Input(description="Main niche", default="educational"),
        num_keywords: int = Input(description="Number of keywords", default=25)
    ) -> str:
        tags = [tag.strip().lower().replace("#", "") for tag in seed_hashtags.split(",") if tag.strip()]
        
        templates = [
            "{tag} 2026", "how to {tag} for students", "best {tag} tips 2026",
            "{tag} hacks for beginners", "{tag} study tips", "{tag} for college students 2026",
            "stop missing {tag} opportunities", "7 reasons you need {tag}"
        ]
        
        keywords = []
        for i in range(num_keywords):
            tag = tags[i % len(tags)] if tags else niche
            template = templates[i % len(templates)]
            kw = template.format(tag=tag)
            keywords.append(f"{i+1}. \"{kw}\"")
        
        output = f"""🚀 SMALL CHANNEL HUNTER ROBOT
Niche: {niche}

=== KEYWORDS TO PASTE IN YOUTUBE ===
""" + "\n".join(keywords) + f"""

=== HOW TO USE ===
1. Paste one keyword in YouTube
2. Filter → Upload date: This month
3. Find videos with 10–300 views
4. Click channel → check subs <5000 and bad thumbnails
5. Offer free gift thumbnail → $4 if they like

Ready to find small educational channels!"""
        
        return output
