from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        "{{first_name}} {{last_name}}",
        "{{first_name}} {{last_name}}",
        "{{last_name}} {{first_name}}",
    )

    # https://www.bachpan.com/baby-names/gujarati/hindu/boy/k
    # https://www.behindthename.com/names/gender/masculine/usage/gujarati
    first_names_male = (
        "કાન્હા",
        "કૃશાંગ",
        "કૃષ્ણ",
        "અભિષેક",
        "અજય",
        "અક્ષય",
        "આનંદ",
        "અનિલ",
        "અંકિત",
        "અર્જુન",
        "અરુણ",
        "આશિષ",
        "અશોક",
        "ભારત",
        "બ્રિજેશ",
        "ચેતન",
        "ચિરાગ",
        "દર્શન",
        "દીપા",
        "દીપક",
        "ધવલ",
        "દિલીપ",
        "દિનેશ",
        "દીપા",
        "દીપક",
        "હરીશ",
        "હર્ષ",
        "હર્ષલ",
        "હીરા",
        "જગદીશ",
        "જય",
        "જયેશ",
        "જિતેન્દ્ર",
        "કાજલ",
        "કમલ",
        "કરણ",
        "કિરણ",
        "કિશન",
        "કૃષ્ણ",
        "કુમાર",
        "કુનાલ",
        "મહેન્દ્ર",
        "મહેશ",
        "મનોજ",
        "મયૂર",
        "મિતુલ",
        "મુકેશ",
        "નરેન્દ્ર",
        "નીરજ",
        "નિખિલ",
        "નીરજ",
        "નીરવ",
        "નિશાંત",
        "નિતિન",
        "પંકજ",
        "પાર્થ",
        "પ્રકાશ",
        "પ્રણવ",
        "પ્રતિક",
        "પ્રવીણ",
        "રાહુલ",
        "રાજ",
        "રાજેન્દ્ર",
        "રાજેશ",
        "રાકેશ",
        "રમેશ",
        "રવિ",
        "રોહિત",
        "સચિન",
        "સમીર",
        "સમીર",
        "સંદિપ",
        "સંજય",
        "સંજીવ",
        "શેખર",
        "સિદ્ધાર્થ",
        "સુભાષ",
        "સુનીલ",
        "સૂરજ",
        "તુષાર",
        "વસંત",
        "વિક્રમ",
        "વિપુલ",
        "વિરાજ",
        "વિશાલ",
        "વિવેક",
        "યશ",
        "ખાદીર",
        "ખગેન્દ્ર",
        "ખગેશ",
        "ખલીફા",
        "ખમીશ",
        "ખાનામ",
        "ખાનીશ",
        "ખર",
        "ખરાધ્વામ્સીને",
        "ખરબંદા",
        "ખાસમ",
        "ખાતિરાવન",
        "ખટવાંગીન",
        "ખાત્વિક",
        "ખ઼જ઼ાના",
        "ખેમચંદ",
        "ખેમપ્રકાશ",
        "ખેમરાજ",
        "ખિયન",
        "ખીલેશ્વર",
        "ખિષન્તં",
        "ખોસલ",
        "ખુનીષ",
        "ખ્સીતીજ",
        "ખુન્દમીર",
        "ખુશમિત",
        "ખુશવેંદ્ર",
        "તથાથાન",
    )

    # https://www.behindthename.com/names/gender/feminine/usage/gujarati
    first_names_female = (
        "અંકિતા",
        "અવની",
        "હીરા",
        "કાજલ",
        "કિરણ",
        "નેહા",
        "નિશા",
        "પૂજા",
        "પ્રાચી",
        "પ્રીતિ",
        "પ્રીતિ",
        "પૂજા",
        "રચના",
        "રાધા",
        "રાધીકા",
        "શ્રેયા",
        "શ્વેતા",
        "સોનલ",
        "તન્વી",
        "તેજલ",
        "ઉર્વી",
        "વર્ષા",
    )

    first_names = first_names_male + first_names_female

    # https://surnames.behindthename.com/submit/names/usage/gujarati
    last_names = (
        "અંટાળા",
        "અર્જુન",
        "અશોક",
        "ભગત",
        "ભંડારી",
        "ભટ્ટ",
        "ભાવસાર",
        "ભાવસાર",
        "ભટ્ટ",
        "ચૌધરી",
        "ચૌહાણ",
        "દવે",
        "દીપક",
        "દેસાઈ",
        "દોશી",
        "ગાંધી",
        "હીરા",
        "જાની",
        "ઝા",
        "ઝાલા",
        "કાજલ",
        "કપાડિયા",
        "ખત્રી",
        "કોઠારી",
        "કુંભાર",
        "લાખાણી",
        "મહાજન",
        "મહારાજ",
        "મહેશ",
        "માળી",
        "મનોજ",
        "મહેતા",
        "નારાયણ",
        "નાયક",
        "ઓઝા",
        "ઓઝા",
        "પાંડે",
        "પાંડે",
        "પંડ્યા",
        "પરમાર",
        "પરમાર",
        "પાઠક",
        "રડ્ઝા",
        "રાજા",
        "રાજાહ",
        "રાજલ",
        "રાજેશ્વરન",
        "રામાણી",
        "રમેશ",
        "રાણા",
        "રાઠોડ",
        "રાવળ",
        "રોશન",
        "સાગર",
        "સાહુ",
        "શાહ",
        "શ્રોફ",
        "શુક્લ",
        "સોલંકી",
        "સુથાર",
        "ઠાકર",
        "ઠક્કર",
        "ઠાકુર",
        "ત્રિવેદી",
        "ઉપાધ્યાય",
        "વિદ્યાની",
        "વિક્રમ",
        "વિવેક",
        "યાદવ",
    )
