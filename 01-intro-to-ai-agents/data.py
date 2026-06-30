"""
Reference data for the DR Film Production Agent.
Source: Lantica Studios, La Casita Films, Law 108-10 (DGCINE).
"""

PRODUCTIONS = [
    {
        "title": "Old",
        "year": 2021,
        "type": "movie",
        "studio": "Universal Pictures",
        "location": "Playa El Valle, Samaná",
        "director": "M. Night Shyamalan",
        "stars": ["Gael García Bernal", "Vicky Krieps", "Rufus Sewell"],
        "service_company": "Lantica Studios",
    },
    {
        "title": "The Lost City",
        "year": 2022,
        "type": "movie",
        "studio": "Paramount Pictures",
        "location": "Monumento Natural Salto De Socoa, Monte Plata",
        "director": "Aaron Nee & Adam Nee",
        "stars": ["Sandra Bullock", "Channing Tatum", "Brad Pitt"],
        "service_company": "Lantica Studios",
    },
    {
        "title": "Shotgun Wedding",
        "year": 2022,
        "type": "movie",
        "studio": "Mandeville Films",
        "location": "Playa Caletón, María Trinidad Sánchez",
        "director": "Jason Moore",
        "stars": ["Jennifer Lopez", "Josh Duhamel", "Lenny Kravitz"],
        "service_company": "Lantica Studios",
    },
    {
        "title": "Arthur the King",
        "year": 2024,
        "type": "movie",
        "studio": "Lionsgate / eOne Films",
        "location": "Zona Colonial, Santo Domingo",
        "director": "Baltazar Kormakur",
        "stars": ["Mark Wahlberg", "Simu Liu"],
        "service_company": "Lantica Studios",
    },
    {
        "title": "Nyad",
        "year": 2023,
        "type": "movie",
        "studio": "Netflix",
        "location": "Centro Acuático, Santo Domingo",
        "director": "Jimmy Chin & Elizabeth Chai Vasarhelyi",
        "stars": ["Annette Bening", "Jodie Foster"],
        "service_company": "Lantica Studios",
    },
    {
        "title": "Hotel Cocaine",
        "year": 2024,
        "type": "series",
        "studio": "MGM+ Studios",
        "location": "Juan Dolio, San Pedro de Macorís",
        "director": "Guillermo Navarro",
        "stars": ["Danny Pino", "Michael Chiklis"],
        "service_company": "Lantica Studios",
    },
    {
        "title": "Narco-Saints",
        "year": 2022,
        "type": "series",
        "studio": "Netflix",
        "location": "Mirador Cachón de la Rubia, Santo Domingo",
        "director": "Yoon Jong-Bin",
        "stars": ["Park Hae-soo", "Jo Woo-jin"],
        "service_company": "Lantica Studios",
    },
    {
        "title": "Sin Límites",
        "year": 2022,
        "type": "series",
        "studio": "Amazon Prime Video",
        "location": "Samaná",
        "director": "Simon West",
        "stars": ["José Coronado", "Álvaro Mel"],
        "service_company": "Lantica Studios",
    },
    {
        "title": "The Killer",
        "year": 2023,
        "type": "movie",
        "studio": "Netflix",
        "location": "Ciudad Colonial, Santo Domingo",
        "director": "David Fincher",
        "stars": ["Michael Fassbender", "Charlize Theron"],
        "service_company": "Lantica Studios",
    },
]


INCENTIVES = {
    "law": "Law 108-10, Article 39 — Modified by Law 82-13 (June 18, 2013)",
    "administered_by": "DGCINE (Dirección General de Cine)",
    "tax_credit": "25% transferable tax credit on all qualified production expenses",
    "minimum_spend": "USD 500,000",
    "qualifying_expenses": [
        "Pre-production, production, and post-production expenses",
        "Equipment rentals",
        "Local and foreign crew (subject to Dominican crew participation)",
        "Location fees",
        "Services and goods purchased in the DR",
    ],
    "dominican_crew_requirement": "25% minimum (from year 6 of the law onward)",
    "validation_timeline": {
        "dgcine_review": "30 calendar days",
        "full_process_max": "90 calendar days",
    },
    "credit_transferability": "Fully transferable to any natural or legal person",
    "additional_benefits": [
        "18% VAT exemption on production-related expenses",
        "Temporary import of goods and equipment",
    ],
    "notes": (
        "Credits can be used to offset income tax (ISR) "
        "or transferred. Cannot be combined with other incentives "
        "for the same production."
    ),
}


SERVICES = [
    {
        "category": "studio",
        "name": "Lantica Studios",
        "website": "lanticastudios.com",
        "location": "Juan Dolio, San Pedro de Macorís",
        "description": (
            "Full-service production studio. One-stop shop for filming in the DR. "
            "Offers sound stages, water tank, underwater filming facilities, "
            "crew sourcing, location scouting, budgeting, and scheduling. "
            "Has serviced over 60 international productions."
        ),
        "notable_credits": ["Old", "The Lost City", "Nyad", "Hotel Cocaine", "Road House"],
    },
    {
        "category": "studio",
        "name": "La Casita Films",
        "website": "lacasitafilms.com",
        "location": "Santo Domingo",
        "description": (
            "Full film production services: locations, permits, local crew, "
            "equipment, logistics, and line production. "
            "Specializes in connecting international productions with DR infrastructure."
        ),
        "notable_credits": ["Dominican independent and international co-productions"],
    },
    {
        "category": "post_production",
        "name": "Pulpo Post",
        "website": "pulpopost.com",
        "location": "Santo Domingo",
        "description": (
            "Full post-production studio. Services include sound design, "
            "pre-mix, final mix, music composition, dubbing, editing, "
            "color correction, DCP & DCDM, LTO backup, and DIT on set. "
            "Has worked with Netflix, Amazon, Disney, HBO, and Sony Pictures Television."
        ),
    },
    {
        "category": "post_production",
        "name": "La Nave Post Lab",
        "website": "lanavepostlab.com.do",
        "location": "Dominican Republic",
        "description": (
            "Post-production laboratory offering color grading, "
            "finishing, and digital cinema deliverables."
        ),
    },
    {
        "category": "equipment",
        "name": "KC Ettes",
        "website": "kcettes.com",
        "location": "Dominican Republic",
        "description": (
            "Camera and grip equipment rental house. "
            "Serves local and international productions."
        ),
    },
    {
        "category": "equipment",
        "name": "PJ Gaffers",
        "website": "pjgaffers.com",
        "location": "Dominican Republic",
        "description": (
            "Lighting and electrical equipment rental. "
            "Specialized gaffer services for film and TV productions."
        ),
    },
]