import matplotlib.pyplot as plt
import numpy

def example():
    dataset1 = [100,140,180,220,300]
    dataset2 = [200,300,400,500,600]

 
    print("Q1, Q2, Q3 ",dataset1," est : ",numpy.quantile(dataset1,numpy.array([0.25, 0.50, 0.75])))
    print("Q1, Q2, Q3 ",dataset2," est : ",numpy.quantile(dataset2,numpy.array([0.25, 0.50, 0.75])))

  
    plt.figure()
    plt.boxplot([dataset1,dataset2])
    plt.title('dataset 1 and 2')
   
    output_file = '/home/do501389/Downloads/boxplot_output.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"Plot saved to: {output_file}")

def ex1():
    dataset1 = [1000, 1100, 1300, 1600, 1800]
    dataset2 = dataset1[:-1] + [3000]
    
    print (dataset1)
    print (dataset2)
    print("Moyenne de la a:", numpy.mean(dataset1))
    print ("Mediane de b :", numpy.median(dataset1))
    print("Moyenne de la b:", numpy.mean(dataset2))
    print ("Mediane de b :", numpy.median(dataset2))

    plt.figure()
    plt.boxplot([dataset1, dataset2])
    plt.title('dataset 1 and 2')
    plt.axhline(numpy.mean(dataset1), color='red', linestyle='--', label='Mean of dataset1')
    plt.axhline(numpy.mean(dataset2), color='blue', linestyle='--', label='Mean of dataset2')


    output_file = '/home/do501389/Downloads/exercise1_output.png'
    plt.savefig(output_file, dpi=200, bbox_inches='tight')
    print(f"Plot saved to: {output_file}")

def  ex2 (): 
    serie1 = [1000, 1100, 1300, 1600, 1800]
    serie2 = [1000, 1100, 1300, 1600, 3000]
    
    
    print("Q1, mediane , Q3 ",serie1," est : ",numpy.quantile(serie1,numpy.array([0.25, 0.50, 0.75])))
    print("Q1, mediane, Q3 ",serie2," est : ",numpy.quantile(serie2,numpy.array([0.25, 0.50, 0.75])))
    
    plt.figure()
    plt.boxplot([serie1, serie2])
    plt.title('serie 1 and 2')
    plt.axhline(numpy.median(serie1), color='red', linestyle='--', label='mediane de serie1')
    plt.axhline(numpy.median(serie2), color='blue', linestyle='--', label='mediane de serie2')
    plt.axhline(numpy.quantile(serie1, 0.25), color='orange', linestyle='--', label='Q1 de serie1')
    plt.axhline(numpy.quantile(serie1, 0.75), color='green', linestyle='--', label='Q3 de serie1')
    plt.axhline(numpy.quantile(serie2, 0.25), color='purple', linestyle='--', label='Q1 de serie2')
    plt.axhline(numpy.quantile(serie2, 0.75), color='brown', linestyle='--', label='Q3 de serie2')
    plt.axhline(numpy.mean(serie1), color='cyan', linestyle='--', label='Moyenne of serie1')
    plt.axhline(numpy.mean(serie2), color='magenta', linestyle='--', label='Moyenne of serie2')
    plt.legend(loc='upper right')


    output_file = '/home/do501389/Downloads/exercise2_output.png'
    plt.savefig(output_file, dpi=200, bbox_inches='tight')
    print(f"Plot saved to: {output_file}")
    # dans cet function, nous avons calculé les quartiles et la médiane pour deux séries de données, puis nous avons créé un boxplot pour visualiser ces statistiques.
    # Nous avons également ajouté des lignes horizontales pour indiquer 
    # les positions des quartiles, de la médiane et de la moyenne pour chaque série.
    # Enfin, nous avons sauvegardé le graphique dans un fichier PNG.
    

def mediane_quartiles_avec_effectifs1(values):
    values2 = []
    for valeur, effectif in values:
        values2.extend([valeur] * effectif)
    quantiles = numpy.quantile(values2, numpy.array([0.25, 0.50, 0.75]))
    return list(quantiles)

def mediane_quartiles_avec_effectifs2(values):
    expanded_values = []
    for valeur, effectif in values:
        expanded_values.extend([valeur] * effectif)
    
    expanded_values.sort()
    
    n = len(expanded_values)
    
    q1_pos = (n + 1) / 4
    median_pos = (n + 1) / 2
    q3_pos = 3 * (n + 1) / 4
    
    def get_value_at_position(pos, sorted_values):
        if pos <= 1:
            return sorted_values[0]
        if pos >= len(sorted_values):
            return sorted_values[-1]
        
        lower_idx = int(pos) - 1
        upper_idx = lower_idx + 1
        fraction = pos - (lower_idx + 1)
        
        if upper_idx >= len(sorted_values):
            return sorted_values[-1]
        
        lower_val = sorted_values[lower_idx]
        upper_val = sorted_values[upper_idx]
        
        return lower_val + fraction * (upper_val - lower_val)
    
    q1 = get_value_at_position(q1_pos, expanded_values)
    median = get_value_at_position(median_pos, expanded_values)
    q3 = get_value_at_position(q3_pos, expanded_values)
    
    return [q1, median, q3]

def ex3():
    values = [[175,1],[180,1],[185,2],[190,2],[195,4],[200,5],[205,5],[210,4],[215,3],[220,1],[225,1],[230,1]]

    print(" numpy.quantile")
    q1_m1, median_m1, q3_m1 = mediane_quartiles_avec_effectifs1(values)
    print(f"Q1: {q1_m1}, Mediane: {median_m1}, Q3: {q3_m1}")

    print("\n(n+1)/4 method ")
    q1_m2, median_m2, q3_m2 = mediane_quartiles_avec_effectifs2(values)
    print(f"Q1: {q1_m2}, Mediane: {median_m2}, Q3: {q3_m2}")

    expanded_values = []
    for valeur, effectif in values:
        expanded_values.extend([valeur] * effectif)
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.boxplot(expanded_values, vert=False)
    plt.title(' numpy.quantile')
    plt.axvline(q1_m1, color='orange', linestyle='--', linewidth=2, label='Q1')
    plt.axvline(median_m1, color='blue', linestyle='--', linewidth=2, label='Mediane')
    plt.axvline(q3_m1, color='green', linestyle='--', linewidth=2, label='Q3')
    plt.legend(loc='upper right')
    
    plt.subplot(1, 2, 2)
    plt.boxplot(expanded_values, vert=False)
    plt.title('(n+1)/4 method')
    plt.axvline(q1_m2, color='orange', linestyle='--', linewidth=2, label='Q1')
    plt.axvline(median_m2, color='blue', linestyle='--', linewidth=2, label='Mediane')
    plt.axvline(q3_m2, color='green', linestyle='--', linewidth=2, label='Q3')
    plt.legend(loc='upper right')
    
    output_file = '/home/do501389/Downloads/exercise3_output.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    


def exercice4(classes, values):
    total_freq = sum(values)
    
    cumulative = [0]
    for v in values:
        cumulative.append(cumulative[-1] + v)
    
    def find_quartile(position):
        for i, cum_freq in enumerate(cumulative[:-1]):
            if position <= cumulative[i + 1] and position > cumulative[i]:
                Li = classes[i][0]
                Ii = classes[i][1] - classes[i][0]
                fi = values[i]
                Fi_minus_1 = cumulative[i]
                return Li + (position - Fi_minus_1) / fi * Ii
        return classes[-1][1]
    
    q1_pos = (total_freq + 1) / 4
    median_pos = (total_freq + 1) / 2
    q3_pos = 3 * (total_freq + 1) / 4
    
    q1 = find_quartile(q1_pos)
    median = find_quartile(median_pos)
    q3 = find_quartile(q3_pos)
    
    return [q1, median, q3]

def exercice4_tests():
   
    
    print("\nA) Ex doc ")
    classes1 = [[0, 150], [150, 160], [160, 170], [170, 180], [180, 200]]
    values1 = [0, 3, 11, 8, 3]
    q1, median, q3 = exercice4(classes1, values1)
    print(f"Classes: {classes1}")
    print(f"Eff: {values1}")
    print(f"Tot: {sum(values1)}")
    print(f"Q1 = {q1:.2f}")
    print(f"Mediane = {median:.2f}")
    print(f"Q3 = {q3:.2f}")
    
    print("\nB) database ")
    classes_db = [[30, 40], [40, 50], [50, 60], [60, 70], [70, 80]]
    values_db = [2, 5, 8, 11, 4]
    q1_db, median_db, q3_db = exercice4(classes_db, values_db)
    print(f"Classes (ms): {classes_db}")
    print(f"Eff: {values_db}")
    print(f"Tot: {sum(values_db)}")
    print(f"Q1 = {q1_db:.2f} ms")
    print(f"Median = {median_db:.2f} ms")
    print(f"Q3 = {q3_db:.2f} ms")
    
    print("\nC) SLA eval")
    print(f"Q3 de bd = {q3_db:.2f} ms")
    if q3_db <= 65:
       
        print(f"The 75% sont exec dans {q3_db:.2f} ms, donc cest <= 65 ms")
    else:
        
        print(f"The 75% sont exec dans  {q3_db:.2f} ms,ce que est > 65 ms")
        print("L'infrastructure actuelle de la base de données ne respecte pas le contrat de service (SLA).")

# L'infrastructure actuelle de la base de données ne respecte pas le contrat de service (SLA). 
# Avec 75% des requêtes prenant 67,50 ms au lieu des 65 ms requis.


def probleme1():
    import pandas as pd
    
    data = pd.read_csv('/home/do501389/Downloads/donnees_pyramide_act.csv', 
                       names=['year', 'gender', 'age', 'frequency'])
    
    years = sorted(data['year'].unique())
    medians_M = []
    medians_F = []
    means_M = []
    means_F = []
    
    for year in years:
        for gender in ['M', 'F']:
            year_gender = data[(data['year'] == year) & (data['gender'] == gender)]
            
            if len(year_gender) == 0:
                continue
            
            ages = year_gender['age'].values.astype(float)
            freqs = year_gender['frequency'].values.astype(float)
            
            total_freq = freqs.sum()
            
            weighted_mean = (ages * freqs).sum() / total_freq
            
            cumsum = numpy.cumsum(freqs)
            median_pos = total_freq / 2
            median_idx = numpy.searchsorted(cumsum, median_pos)
            median = ages[median_idx]
            
            if gender == 'M':
                medians_M.append(float(median))
                means_M.append(float(weighted_mean))
            else:
                medians_F.append(float(median))
                means_F.append(float(weighted_mean))
    
    m1_2023 = medians_M[-1]
    m2_2023 = medians_F[-1]
    
    print("="*60)
    print("PROBLEME 1: Age Median of French Population")
    print("="*60)
    print(f"\n2023 Results:")
    print(f"Median age (Male) m1 = {m1_2023:.2f} years")
    print(f"Median age (Female) m2 = {m2_2023:.2f} years")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    ax1.plot(years, means_M, 'r-', linewidth=2, label='Mean (Male)')
    ax1.plot(years, medians_M, 'r--', linewidth=2, label='Median (Male)')
    ax1.plot(years, means_F, 'b-', linewidth=2, label='Mean (Female)')
    ax1.plot(years, medians_F, 'b--', linewidth=2, label='Median (Female)')
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Age (years)', fontsize=12)
    ax1.set_title('Evolution of Mean and Median Ages (1991-2023)', fontsize=12, fontweight='bold')
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(1990, 2024)
    
    data_2023 = data[data['year'] == 2023]
    ages_M_2023 = []
    ages_F_2023 = []
    
    for _, row in data_2023.iterrows():
        if row['gender'] == 'M':
            ages_M_2023.extend([row['age']] * int(row['frequency']))
        else:
            ages_F_2023.extend([row['age']] * int(row['frequency']))
    
    bp = ax2.boxplot([ages_M_2023, ages_F_2023], labels=['Male', 'Female'], vert=True, patch_artist=True)
    for patch, color in zip(bp['boxes'], ['lightcoral', 'lightblue']):
        patch.set_facecolor(color)
    
    mean_M_2023 = numpy.mean(ages_M_2023)
    mean_F_2023 = numpy.mean(ages_F_2023)
    
    ax2.scatter([1], [mean_M_2023], color='red', s=100, marker='D', label=f'Mean (M): {mean_M_2023:.1f}', zorder=5)
    ax2.scatter([2], [mean_F_2023], color='blue', s=100, marker='D', label=f'Mean (F): {mean_F_2023:.1f}', zorder=5)
    
    ax2.set_ylabel('Age (years)', fontsize=12)
    ax2.set_title('Boxplot - 2023 Age Distribution with Means', fontsize=12, fontweight='bold')
    ax2.legend(loc='best')
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    output_file = '/home/do501389/Downloads/probleme1_output.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"\nGraphs saved to: {output_file}")
    
    print("\n" + "="*60)
    print("ANALYSIS AND COMMENTARY:")
    print("="*60)
    print(f"\n1. Are mean and median ages identical between genders?")
    print(f"   Male:   Mean = {mean_M_2023:.2f} years, Median = {m1_2023:.2f} years (Diff: {abs(mean_M_2023 - m1_2023):.2f})")
    print(f"   Female: Mean = {mean_F_2023:.2f} years, Median = {m2_2023:.2f} years (Diff: {abs(mean_F_2023 - m2_2023):.2f})")
    print(f"   Conclusion: The mean and median are DIFFERENT for both genders.")
    
    evolution_M = m1_2023 - medians_M[0]
    evolution_F = m2_2023 - medians_F[0]
    
    print(f"\n2. How has median age evolved from 1991 to 2023?")
    print(f"   Male:   {medians_M[0]:.2f} years (1991) → {m1_2023:.2f} years (2023) [+{evolution_M:.2f} years]")
    print(f"   Female: {medians_F[0]:.2f} years (1991) → {m2_2023:.2f} years (2023) [+{evolution_F:.2f} years]")
    print(f"   Conclusion: Median ages have INCREASED for both genders, indicating population aging.")
    
    print(f"\n3. Answer to the problematic:")
    print(f"   The French population is AGING significantly. Over 32 years (1991-2023):")
    print(f"   - Male median age increased by {evolution_M:.2f} years ({evolution_M/medians_M[0]*100:.1f}%)")
    print(f"   - Female median age increased by {evolution_F:.2f} years ({evolution_F/medians_F[0]*100:.1f}%)")
    print(f"   - Categories: Senior population (65+) increasing, children proportion declining")
    print(f"   - Policy implications: Healthcare, pensions, and workforce planning adjustments needed")
    
    return medians_M, medians_F
    print(f"Median age de homme  m1 = {m1_2023:.2f} ans ")
    print(f"Median age de femme m2 = {m2_2023:.2f} ans")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    ax1.plot(years, means_H, 'r-', linewidth=2, label='Mean homme ')
    ax1.plot(years, medians_H, 'r--', linewidth=2, label='Median homme')
    ax1.plot(years, means_F, 'b-', linewidth=2, label='Mean femme')
    ax1.plot(years, medians_F, 'b--', linewidth=2, label='Median femme')
    ax1.set_xlabel('Année', fontsize=12)
    ax1.set_ylabel('Age (years)', fontsize=12)
    ax1.set_title('Evolution des ages medianes entre (1991-2023)', fontsize=12, fontweight='bold')
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(1990, 2024)
    
    data_2023 = data[data['age'] == 2023]
    ages_H_2023 = []
    ages_F_2023 = []
    
    for _, row in data_2023.iterrows():
        if row['gender'] == 'H':
            ages_H_2023.extend([row['age']] * int(row['freq']))
        else:
            ages_F_2023.extend([row['age']] * int(row['freq']))
    
    bp = ax2.boxplot([ages_H_2023, ages_F_2023], labels=['homme', 'femme'], vert=True, patch_artist=True)
    for patch, color in zip(bp['boxes'], ['lightcoral', 'lightblue']):
        patch.set_facecolor(color)
    
    mean_H_2023 = numpy.mean(ages_H_2023)
    mean_F_2023 = numpy.mean(ages_F_2023)
    
    ax2.scatter([1], [mean_H_2023], color='red', s=100, marker='D', label=f'Mean (H): {mean_H_2023:.1f}', zorder=5)
    ax2.scatter([2], [mean_F_2023], color='blue', s=100, marker='D', label=f'Mean (F): {mean_F_2023:.1f}', zorder=5)
    
    ax2.set_ylabel('Age (years)', fontsize=12)
    ax2.set_title('Boxplot - 2023 Age Distribution with Means', fontsize=12, fontweight='bold')
    ax2.legend(loc='best')
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    output_file = '/home/do501389/Downloads/probleme1_output.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"\nGraphs saved to: {output_file}")
    
    
    print(f"\n1. Are mean and median ages identical between genders?")
    print(f"   Male:   Mean = {mean_H_2023:.2f} years, Median = {m1_2023:.2f} years (Diff: {abs(mean_H_2023 - m1_2023):.2f})")
    print(f"   Female: Mean = {mean_F_2023:.2f} years, Median = {m2_2023:.2f} years (Diff: {abs(mean_F_2023 - m2_2023):.2f})")
    print(f"   Conclusion: The mean and median are DIFFERENT for both genders.")
    
    evolution_H = m1_2023 - medians_H[0]
    evolution_F = m2_2023 - medians_F[0]
    
    print(f"\n2. How has median age evolved from 1991 to 2023?")
    print(f"   Male:   {medians_H[0]:.2f} years (1991) → {m1_2023:.2f} years (2023) [+{evolution_H:.2f} years]")
    print(f"   Female: {medians_F[0]:.2f} years (1991) → {m2_2023:.2f} years (2023) [+{evolution_F:.2f} years]")
    print(f"   Conclusion: Median ages have INCREASED for both genders, indicating population aging.")
    
    print(f"\n3. Answer to the problematic:")
    print(f"   The French population is AGING significantly. Over 32 years (1991-2023):")
    print(f"   - Male median age increased by {evolution_H:.2f} years ({evolution_H/medians_H[0]*100:.1f}%)")
    print(f"   - Female median age increased by {evolution_F:.2f} years ({evolution_F/medians_F[0]*100:.1f}%)")
    print(f"   - Categories: Senior population (65+) increasing, children proportion declining")
    print(f"   - Policy implications: Healthcare, pensions, and workforce planning adjustments needed")
    
    return medians_H, medians_F

if __name__ == "__main__":
    ex1()
    ex2()
    ex3()
    exercice4_tests()
    probleme1()
    
