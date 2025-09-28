# 🚀 Руководство по запуску проекта

## Быстрый старт

### 1. Подготовка окружения

```bash
# Клонировать репозиторий
git clone https://github.com/aibalasy1/air-quality-analysis.git
cd air-quality-analysis

# Установить зависимости
pip install -r requirements.txt

# Запустить Jupyter Notebook
jupyter notebook
```

### 2. Порядок выполнения

#### Шаг 1: Предобработка данных
```bash
# Открыть и выполнить preprocessing.ipynb
jupyter notebook preprocessing.ipynb
```

**Что делает этот notebook:**
- ✅ Загружает данные из `updated_dataset/filtered_dataset.xlsx`
- ✅ Интегрирует метеоданные из `weatherapi/new/`
- ✅ Создает временные метки и сезонные переменные
- ✅ Обрабатывает пропущенные значения
- ✅ Сохраняет результат в `airdata_updated.csv`

#### Шаг 2: Анализ временных рядов
```bash
# Открыть и выполнить Analysis of time variables.ipynb
jupyter notebook "Analysis of time variables.ipynb"
```

**Что делает этот notebook:**
- ✅ FFT анализ для выявления циклов в данных
- ✅ Тест Гранжера на причинность
- ✅ Создание оптимальных лаговых переменных
- ✅ Экспорт датасетов в `upd_sep_targets/` и `upd_sep_targets_with_lags/`

#### Шаг 3: Основное моделирование
```bash
# Открыть и выполнить Рабочая версия .ipynb
jupyter notebook "Рабочая версия .ipynb"
```

**Что делает этот notebook:**
- ✅ Загружает данные с лаговыми переменными
- ✅ Отбирает значимые признаки (Lasso, ElasticNet)
- ✅ Визуализирует важность признаков
- ✅ Удаляет выбросы
- ✅ Строит финальные модели

## 📊 Ожидаемые результаты

### После предобработки:
- Файл `airdata_updated.csv` с чистыми данными
- Интеграция метеоданных для всех станций

### После анализа временных рядов:
- 5 отдельных файлов в `upd_sep_targets/`
- 5 файлов с лагами в `upd_sep_targets_with_lags/`
- Графики FFT анализа
- Результаты тестов Гранжера

### После моделирования:
- Таблицы важности признаков
- Визуализации отобранных переменных
- Датасеты без выбросов
- Готовые модели для каждого загрязнителя

## 🔧 Решение проблем

### Проблема: ModuleNotFoundError
```bash
# Установить отсутствующие пакеты
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### Проблема: Файлы данных не найдены
Убедитесь, что структура папок соответствует описанной в `PROJECT_STRUCTURE.md`

### Проблема: Ошибки кодировки
```python
# В начале каждого notebook добавить:
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
```

### Проблема: Предупреждения pandas
```python
# Отключить предупреждения (если нужно)
import warnings
warnings.filterwarnings('ignore')
```

## 📈 Кастомизация

### Изменение параметров анализа
В `Analysis of time variables.ipynb`:
```python
# Изменить параметры FFT анализа
fft_lags_dict = {
    'CO':    [1, 6],      # можно изменить лаги
    'NO':    [0.5, 1, 9],
    'PM10':  [1],
    'PM2.5': [1],
    'SO2':   [6]
}
```

### Изменение методов отбора признаков
В `Рабочая версия .ipynb`:
```python
# Выбор метода регуляризации
selected_co = select_features_by_model(data_co, target="CO", method="lasso")
# или
selected_co = select_features_by_model(data_co, target="CO", method="elasticnet")
```

## 🎯 Финальные выходные файлы

После полного выполнения всех notebook'ов у вас будут:

1. **Обработанные данные:**
   - `airdata_updated.csv`
   - Файлы в `upd_sep_targets_with_lags/`

2. **Визуализации:**
   - Графики важности признаков
   - FFT спектры
   - Диаграммы распределений

3. **Готовые датасеты для моделирования:**
   - Отфильтрованные и очищенные от выбросов
   - С отобранными значимыми признаками

## 📞 Поддержка

Если возникают проблемы:
1. Проверьте версии пакетов в `requirements.txt`
2. Убедитесь в правильности путей к файлам
3. Проверьте структуру данных
4. Создайте issue в репозитории с описанием проблемы