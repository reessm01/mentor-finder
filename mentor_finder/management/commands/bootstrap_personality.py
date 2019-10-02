from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from mentor_finder.personality.models import Personality

class Command(BaseCommand):
    help = 'Intializes or adds personality types.'

    def handle(self, *args, **options):
        personalities = {
            'INTJ': {
                'detail':'INTJs, as introverts, are quiet, reserved, and comfortable being alone. They are usually self-sufficient and would rather work alone than in a group. Socializing drains an introvert’s energy, causing them to need to recharge. INTJs are interested in ideas and theories. When observing the world they are always questioning why things happen the way they do. They excel at developing plans and strategies, and don’t like uncertainty.',
                'compatible': ['ISFJ', 'ENFJ', 'ENTJ', 'INFJ', 'ENFP', 'INFP', 'ESFJ', 'ESFP', 'ISFP', 'INTP', 'ISTJ', 'ENTP']
                },
            'INTP': {
                'detail':'INTPs are well known for their brilliant theories and unrelenting logic, which makes sense since they are arguably the most logical minded of all the personality types. They love patterns, have a keen eye for picking up on discrepancies, and a good ability to read people, making it a bad idea to lie to an INTP. People of this personality type aren’t interested in practical, day-to-day activities and maintenance, but when they find an environment where their creative genius and potential can be expressed, there is no limit to the time and energy INTPs will expend in developing an insightful and unbiased solution.',
                'compatible': ['ENTP', 'INTP', 'INTJ', 'ESTJ', 'ISTJ', 'ESTP', 'ENTJ', 'ENFJ', 'INFJ', 'ENFP', 'INFP']
                },
            'ENTJ': {
                'detail':'An ENTJ’s primary mode of living focuses on external aspects and all things are dealt with rationally and logically. Their secondary mode of operation is internal, where intuition and reasoning take effect. ENTJs are natural born leaders among the 16 personality types and like being in charge. They live in a world of possibilities and they often see challenges and obstacles as great opportunities to push themselves. They seem to have a natural gift for leadership, making decisions, and considering options and ideas quickly yet carefully. They are “take charge” people who do not like to sit still.',
                'compatible': ['ESTJ', 'ISTP', 'ENTJ', 'ENFJ', 'INTJ', 'ISTJ', 'ESTP', 'ENTP', 'INTP', 'INFJ', 'ENFP']
                },
            'ENTP': {
                'detail':'Those with the ENTP personality are some of the rarest in the world, which is completely understandable. Although they are extroverts, they don’t enjoy small talk and may not thrive in many social situations, especially those that involve people who are too different from the ENTP. ENTPs are intelligent and knowledgeable need to be constantly mentally stimulated. They have the ability to discuss theories and facts in extensive detail. They are logical, rational, and objective in their approach to information and arguments.',
                'compatible': ['ENTP', 'INTP', 'INFJ', 'ESTJ', 'ISTJ', 'ESTP', 'ESFP', 'ENTJ', 'ENFP', 'INFP', 'ENFJ']
                },
            'INFJ': {
                'detail':'INFJs are visionaries and idealists who ooze creative imagination and brilliant ideas. They have a different, and usually more profound, way of looking at the world. They have a substance and depth in the way they think, never taking anything at surface level or accepting things the way they are. Others may sometimes perceive them as weird or amusing because of their different outlook on life.',
                'compatible': ['ENTP', 'ENFP', 'INFJ', 'INFP', 'ENFJ', 'ISFJ', 'ESFP', 'ISFP', 'ENTJ', 'INTJ', 'INTP', 'ISTJ']
                },
            'INFP': {
                'detail':'INFPs, like most introverts, are quiet and reserved. They prefer not to talk about themselves, especially in the first encounter with a new person. They like spending time alone in quiet places where they can make sense of what is happening around them. They love analyzing signs and symbols, and consider them to be metaphors that have deeper meanings related to life. They are lost in their imagination and daydreams, always drowned in the depth of their thoughts, fantasies, and ideas.',
                'compatible': ['ENFP', 'INFP', 'ENFJ', 'INFJ', 'ISFJ', 'ESFJ', 'ESFP', 'ISFP', 'ENTP', 'INTP']
                },
            'ENFJ': {
                'detail':'ENFJs are people-focused individuals. They are extroverted, idealistic, charismatic, outspoken, highly principled and ethical, and usually know how to connect with others no matter their background or personality. Mainly relying on intuition and feelings, they tend to live in their imagination rather than in the real world. Instead of focusing on living in the “now” and what is currently happening, ENFJs tend to concentrate on the abstract and what could possibly happen in the future.',
                'compatible': ['ISFJ', 'ENFJ', 'ENTJ', 'INFJ', 'ENFP', 'INFP', 'ESFJ', 'ESFP', 'ISFP', 'INTP', 'ISTJ', 'ENTP']
                },
            'ENFP': {
                'detail':'ENFPs have an Extraverted, Intuitive, Feeling and Perceiving personality. This personality type is highly individualistic and Champions strive toward creating their own methods, looks, actions, habits, and ideas — they do not like cookie cutter people and hate when they are forced to live inside a box. They like to be around other people and have a strong intuitive nature when it comes to themselves and others. They operate from their feelings most of the time, and they are highly perceptive and thoughtful.',
                'compatible': ['INFJ', 'INFP', 'ENFJ', 'ENFP', 'ESFJ', 'ENTJ', 'ENTP', 'INTJ', 'INTP','ESFP', 'ISFP']
                },
            'ISTJ': {
                'detail':'At first glance, ISTJs are intimidating. They appear serious, formal, and proper. They also love traditions and old-school values that uphold patience, hard work, honor, and social and cultural responsibility. They are reserved, calm, quiet, and upright. These traits result from the combination of I, S, T, and J, a personality type that is often misunderstood.',
                'compatible': ['ESTJ', 'ISTJ', 'INTJ', 'ISTP', 'ESTP' , 'ENTJ', 'INTP', 'ENFJ', 'INFJ', 'ISFJ', 'ISFP', 'ENTP']
                },
            'ISFJ': {
                'detail':'ISFJs are philanthropists and they are always ready to give back and return generosity with even more generosity. The people and things they believe in will be upheld and supported with enthusiasm and unselfishness. ISFJs are warm and kind-hearted. They value harmony and cooperation, and are likely to be very sensitive to other people’s feelings. People value the ISFJ for their consideration and awareness, and their ability to bring out the best in others.',
                'compatible': ['ISFJ', 'ENFJ', 'ESTJ', 'ESFJ', 'ESTP', 'INFJ', 'INFP', 'ESFP', 'ISTJ', 'ISFP']
                },
            'ESTJ': {
                'detail':'ESTJs are organized, honest, dedicated, dignified, traditional, and are great believers of doing what they believe is right and socially acceptable. Though the paths towards “good” and “right” are difficult, they are glad to take their place as the leaders of the pack. They are the epitome of good citizenry. People look to ESTJs for guidance and counsel, and ESTJs are always happy that they are approached for help.',
                'compatible': ['ISTJ', 'ESFJ', 'ISFJ', 'ENTJ', 'INTJ', 'ISTP', 'ENTP', 'INTP', 'ESTP', 'ESFP', 'ISFP']
                },
            'ESFJ': {
                'detail':'ESFJs are the stereotypical extroverts. They are social butterflies, and their need to interact with others and make people happy usually ends up making them popular. The ESFJ usually tends to be the cheerleader or sports hero in high school and college. Later on in life, they continue to revel in the spotlight, and are primarily focused on organizing social events for their families, friends and communities. ESFJ is a common personality type and one that is liked by many people.',
                'compatible': ['ESTJ', 'ENFP', 'ISFJ', 'ESFJ', 'ENFJ', 'INFP', 'ISFP', 'ISTP', 'ESFP']
                },
            'ISTP': {
                'detail':'ISTPs are mysterious people who are usually very rational and logical, but also quite spontaneous and enthusiastic. Their personality traits are less easily recognizable than those of other types, and even people who know them well can’t always anticipate their reactions. Deep down, ISTPs are spontaneous, unpredictable individuals, but they hide those traits from the outside world, often very successfully.',
                'compatible': ['ESTJ', 'ISTJ', 'ENTJ', 'ESTP', 'ESFJ', 'ISFP', 'INTJ', 'ISFJ']
                },
            'ISFP': {
                'detail':'ISFPs are introverts that do not seem like introverts. It is because even if they have difficulties connecting to other people at first, they become warm, approachable, and friendly eventually. They are fun to be with and very spontaneous, which makes them the perfect friend to tag along in whatever activity, regardless if planned or unplanned. ISFPs want to live their life to the fullest and embrace the present, so they make sure they are always out to explore new things and discover new experiences. It is in experience that they find wisdom, so they do see more value in meeting new people than other introverts.',
                'compatible': ['ESFP', 'ISFP', 'ESTP', 'ESTJ', 'ESFJ', 'ISTP', 'ENFJ', 'INFJ', 'INFP', 'ISFJ', 'ISTJ', 'ENFP']
                },
            'ESTP': {
                'detail':'ESTPs have an Extraverted, Sensing, Thinking, and Perceptive personality. ESTPs are governed by the need for social interaction, feelings and emotions, logical processes and reasoning, along with a need for freedom. Theory and abstracts don’t keep ESTP’s interested for long. ESTPs leap before they look, fixing their mistakes as they go, rather than sitting idle or preparing contingency plans.',
                'compatible': ['ISTJ', 'ESTP', 'ISTP', 'ESFP', 'ESTJ', 'ISFP', 'ENTJ', 'ENTP', 'INTP', 'ISFJ']
                },
            'ESFP': {
                'detail':'ESFPs have an Extraverted, Observant, Feeling and Perceiving personality, and are commonly seen as Entertainers. Born to be in front of others and to capture the stage, ESFPs love the spotlight. ESFPs are thoughtful explorers who love learning and sharing what they learn with others. ESFPs are “people people” with strong interpersonal skills. They are lively and fun, and enjoy being the center of attention. They are warm, generous, and friendly, sympathetic and concerned for other people’s well-being.',
                'compatible': ['ESTP', 'ISFP', 'ESTJ', 'ESFJ', 'ISFJ', 'ESFP', 'ENTP', 'ENFJ', 'INFJ', 'ENFP', 'INFP']
                }
        }

        added = []
        print(personalities.keys())
        try:
            for key in personalities.keys():
                Personality.objects.create(
                    title=key,
                    detail=personalities[key]['detail']
                )

            added.append(key)

        except IntegrityError:
            pass
        
        self.stdout.write(self.style.SUCCESS(f'Personality table rows added: {added}'))

        edited = []

        try:
            for key in personalities.keys():
                personality = Personality.objects.get(title=key)
                for related in personalities[key]['compatible']:
                    related_personality = Personality.objects.get(title=related)
                    personality.related.add(related_personality)
                personality.save()
                edited.append(key)

        except Exception as error:
            self.stdout.write(self.style.NOTICE(error))

        self.stdout.write(self.style.SUCCESS(f'Personality table rows edited: {edited}'))
        



